# 💻 Web Application for Laptop Recommendation

เว็บแอปพลิเคชันแนะนำแล็ปท็อปด้วย **Rule-based Expert System** —
ผู้ใช้ตอบคำถามทีละขั้น (งบประมาณ → ลักษณะการใช้งาน → ระบบปฏิบัติการ → หน้าจอสัมผัส)
แล้วระบบจะแนะนำแล็ปท็อปที่เหมาะสมที่สุด พร้อมหน้ารายการตามยี่ห้อ ค้นหา กรอง
เรียงลำดับราคา ดูรายละเอียด และเปรียบเทียบแล็ปท็อป 2 เครื่อง

> โปรเจกต์ปัญหาพิเศษ (Senior Project) — refactor ใหม่ให้มีโครงสร้างระดับ Production
> โดยคงหน้าตาและพฤติกรรมของระบบเดิมไว้ทั้งหมด

---

## ✨ Features

- **ระบบแนะนำแล็ปท็อป (Rule-based Expert System)** — ตอบคำถาม 2–4 ขั้น
  ระบบจับคู่คำตอบเข้ากับกฎ 18 ข้อ (Rule 1–18) แล้วแสดงแล็ปท็อปที่เข้าเงื่อนไข
- **เรียกดูตามยี่ห้อ** — Acer, Apple, Asus, Dell, HP, Lenovo, MSI
- **ค้นหา** ตามชื่อรุ่น
- **กรองข้อมูลแบบ Realtime** ตามยี่ห้อ, ช่วงราคา, RAM (4/8/16/32 GB), ความจุ
  (128 GB – 1 TB) — ติ๊กเลือกแล้วรายการบนหน้านั้นถูกกรองทันทีโดยไม่โหลดหน้าใหม่
  และกรองเฉพาะรายการที่แสดงอยู่ (เช่น ในหน้าผลการแนะนำ จะกรองภายใน
  ผลการแนะนำเท่านั้น)
- **เรียงลำดับราคา** ถูก→แพง / แพง→ถูก
- **หน้ารายละเอียด** สเปกครบ ข้อดี–ข้อเสีย และช่องทางซื้อ
- **เปรียบเทียบแล็ปท็อป 2 เครื่อง** แบบเคียงข้างกัน
- **ฟอร์มติดต่อ** ส่งอีเมลผ่าน EmailJS

## 🛠 Technology Stack

| ส่วน | เทคโนโลยี |
| --- | --- |
| Backend | Python 3.10+, Flask (Blueprints + Application Factory) |
| Database | MySQL 5.7+ / MariaDB, SQLAlchemy (parameterized raw SQL) |
| Frontend | Jinja2 Templates (Template Inheritance), HTML/CSS, jQuery |
| Config | python-dotenv (`.env`) |

## 📁 Folder Structure

```
├── run.py                     # จุดเริ่มต้นรันแอป
├── requirements.txt
├── .env.example               # ตัวอย่าง configuration (คัดลอกเป็น .env)
├── app/                       # โค้ดฝั่ง backend
│   ├── __init__.py            # create_app (Application Factory)
│   ├── config.py              # อ่านค่า .env
│   ├── extensions.py          # SQLAlchemy instance
│   ├── models.py              # View models (LaptopSummary / LaptopDetail)
│   ├── repository.py          # Data Access Layer — SQL ทั้งหมดรวมที่เดียว
│   └── routes/
│       ├── main.py            # หน้าแรก / ค้นหา / รายละเอียด / เปรียบเทียบ
│       ├── catalog.py         # รายการตามยี่ห้อ / กรอง / เรียงราคา
│       └── recommendation.py  # ระบบแนะนำ (Rule-based) + โครงสร้างคำถาม
├── templates/                 # Jinja2 templates
│   ├── base.html              # โครงหน้าเว็บหลัก
│   ├── catalog_base.html      # โครงหน้ารายการ (สืบทอดจาก base)
│   ├── brand_list.html        # หน้ารายการรายยี่ห้อ (ไฟล์เดียวใช้ทั้ง 7 ยี่ห้อ)
│   ├── recom_step.html        # หน้าคำถามแนะนำ (ไฟล์เดียวใช้ทั้ง 9 ขั้น)
│   ├── ...                    # หน้าอื่น ๆ
│   └── components/            # ส่วนประกอบที่ใช้ซ้ำ (filter, list, sort, nav ฯลฯ)
├── database/
│   ├── schema.sql             # โครงสร้างฐานข้อมูล (ตาราง + FK + Index)
│   └── example_seed.sql       # ข้อมูลตัวอย่าง "สมมติทั้งหมด" ครอบคลุม Rule 1-18
└── static/                    # CSS / JS / รูปภาพ / ฟอนต์
```

## 🏗 Architecture

แอปแบ่งเป็น 3 ชั้นตามหลัก Separation of Concerns:

1. **Routes (Blueprints)** — รับ request, ตรวจพารามิเตอร์, เลือก template
   - URL แบบไดนามิก เช่น `/<brand>_list` ใช้ view เดียวรองรับทั้ง 7 ยี่ห้อ
     (แทนการเขียนฟังก์ชันแยกยี่ห้อละตัวแบบเดิม) โดย URL เดิมทั้งหมดยังใช้ได้
2. **Repository (Data Access Layer)** — ฟังก์ชัน `fetch_summaries()` เดียว
   ประกอบเงื่อนไข (ยี่ห้อ/rule/ค้นหา/เรียงราคา ฯลฯ) แบบ parameterized
   ทั้งหมด แทน query ซ้ำ ๆ ~80 ฟังก์ชันในโค้ดเดิม ส่วนการกรองบนหน้า
   รายการเป็น client-side realtime filter (ดู `components/filter_panel.html`)
3. **Templates (Jinja2 Inheritance)** — `base.html` → `catalog_base.html` →
   หน้าเพจ ลดไฟล์ HTML ซ้ำจาก 7 หน้า brand + 9 หน้าคำถาม เหลืออย่างละ 1 ไฟล์

**Rule-based Recommendation:** โครงสร้างคำถามอยู่ใน
[app/routes/recommendation.py](app/routes/recommendation.py) เป็น dict `STEPS`
แต่ละตัวเลือกชี้ไปคำถามถัดไปหรือจบที่ `Rule: N` ซึ่งใช้ค้นแล็ปท็อปในคอลัมน์
`laptops.rule` — logic การจับคู่กฎเหมือนระบบเดิมทุกประการ

## 🚀 Installation

ต้องมี: Python 3.10+, MySQL (เช่น XAMPP / MySQL Server)

```bash
# 1) Clone
git clone https://github.com/MildRinrada/Web-Application-For-Laptops-Recommendation.git
cd Web-Application-For-Laptops-Recommendation

# 2) สร้าง virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 3) ติดตั้ง dependencies
pip install -r requirements.txt
```

## ⚙️ Configuration

```bash
# คัดลอกไฟล์ตัวอย่างแล้วแก้ค่าตามเครื่องของคุณ
copy .env.example .env       # Windows
# cp .env.example .env       # macOS/Linux
```

แก้ไข `.env`:

```ini
DB_HOST=localhost
DB_PORT=3306
DB_NAME=laptopdb
DB_USER=root
DB_PASSWORD=รหัสผ่านของคุณ
FLASK_DEBUG=1
```

> 🔒 `.env` ถูก gitignore ไว้แล้ว — ห้าม commit รหัสผ่านหรือ API key ขึ้น Git

## 🗄 Database Setup

```bash
# สร้างฐานข้อมูลและตาราง
mysql -u root -p < database/schema.sql
```

โครงสร้างเป็นแบบ normalized: ตารางหลัก `laptops` อ้างอิงตาราง
`processor`, `graphic`, `memory`, `storage`, `display`, `connection`,
`laptop_store` ผ่าน Foreign Key พร้อม Index ที่คอลัมน์ `brand`, `prices`, `rule`

## 🌱 Sample Data Setup

```bash
mysql -u root -p laptopdb < database/example_seed.sql
```

ข้อมูลตัวอย่าง **เป็นข้อมูลสมมติทั้งหมด** (18 เครื่อง ครอบคลุม Rule 1–18 และครบ
ทั้ง 7 ยี่ห้อ) สร้างขึ้นเพื่อให้ทุกฟีเจอร์มีข้อมูลแสดงผล — ไม่ใช่ข้อมูลจริงจาก
แบบสอบถาม และย้อนกลับไปหาข้อมูลจริงไม่ได้

## ▶️ How to Run

```bash
python run.py
```

เปิดเบราว์เซอร์ที่ http://127.0.0.1:5000

## 🔮 Future Improvements

- เพิ่มระบบจัดการข้อมูลแล็ปท็อป (Admin CRUD) แทนการแก้ข้อมูลผ่าน SQL
- แยกตาราง `rules` และหน้า UI สำหรับปรับเงื่อนไขของ Expert System
- เพิ่ม pagination ในหน้ารายการ และ full-text search
- เขียน unit tests / integration tests (pytest) และตั้ง CI
- ปรับ frontend เป็น responsive เต็มรูปแบบสำหรับมือถือ
- Deploy ด้วย Docker + Gunicorn/Nginx

## 📄 หมายเหตุเรื่องข้อมูล

ข้อมูลจริงจากแบบสอบถาม (ไฟล์ CSV) **ไม่ถูกรวมไว้ใน repository นี้**
เพื่อความเป็นส่วนตัวของผู้ตอบแบบสอบถาม — repository มีเฉพาะข้อมูลตัวอย่างสมมติ
