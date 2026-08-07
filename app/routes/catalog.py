"""หน้ารายการแล็ปท็อปตามยี่ห้อ

URL ของหน้ารายการคงรูปแบบเดิมของระบบไว้ (เช่น /Acer_list) แต่ยุบ handler
ที่ซ้ำกันต่อแบรนด์ให้เหลือ handler เดียวที่รับชื่อแบรนด์เป็นพารามิเตอร์

หมายเหตุ: การกรองและการเรียงลำดับราคาเป็นแบบ realtime ฝั่ง client
(static/js/laptop-list.js) — ทำงานกับรายการที่แสดงบนหน้านั้นโดยตรง
จึงไม่มี endpoint สำหรับกรอง/เรียงลำดับฝั่ง server อีกต่อไป
"""
from flask import Blueprint, render_template

from .. import repository

catalog_bp = Blueprint("catalog", __name__)

# ค่า brand ในฐานข้อมูล
BRANDS = ["Acer", "Apple", "Asus", "Dell", "Hp", "Lenovo", "Msi"]

# ชื่อที่ใช้แสดงผลบนหน้าเว็บ (คงตามหน้าเดิม)
BRAND_DISPLAY = {"Msi": "MSI"}


@catalog_bp.route("/<any(Acer, Apple, Asus, Dell, Hp, Lenovo, Msi):brand>_list")
def brand_list(brand):
    laptops = repository.fetch_summaries(brand=brand)
    return render_template(
        "brand_list.html",
        brand=brand,
        brand_display=BRAND_DISPLAY.get(brand, brand),
        laptops=laptops,
    )
