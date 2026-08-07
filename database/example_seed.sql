-- ============================================================
-- Example Seed Data (ข้อมูลตัวอย่างสมมติทั้งหมด)
--
-- ข้อมูลในไฟล์นี้ถูกสร้างขึ้นเพื่อการสาธิต/พัฒนาเท่านั้น
-- ไม่ใช่ข้อมูลจริงจากแบบสอบถาม และไม่สามารถย้อนกลับไปหาข้อมูลจริงได้
-- รุ่น ราคา สเปก คำอธิบาย และลิงก์ร้านค้า เป็นข้อมูลสมมติ
--
-- ครอบคลุม Rule: 1-18 (หนึ่งเครื่องต่อหนึ่ง rule) เพื่อให้ทุกเส้นทาง
-- ของระบบแนะนำมีผลลัพธ์แสดง และครบทั้ง 7 ยี่ห้อ
--
-- วิธีใช้:  mysql -u root -p < database/schema.sql
--          mysql -u root -p laptopdb < database/example_seed.sql
-- ============================================================

USE laptopdb;

-- ------------------------------------------------------------
-- Lookup tables
-- ------------------------------------------------------------

INSERT INTO processor (processor_id, cpu_brand, cpu_model, base_clock, boost_clock, cache) VALUES
(1, 'Intel', 'Intel Demo Core D3-100',  1.20, 2.80, '4 MB'),
(2, 'Intel', 'Intel Demo Core D5-500',  2.00, 4.20, '8 MB'),
(3, 'Intel', 'Intel Demo Core D7-700',  2.40, 4.80, '16 MB'),
(4, 'AMD',   'AMD Demo R3-3100',        2.10, 3.50, '4 MB'),
(5, 'AMD',   'AMD Demo R5-5500',        2.30, 4.00, '8 MB'),
(6, 'AMD',   'AMD Demo R7-7700',        2.50, 4.50, '16 MB'),
(7, 'Apple', 'Apple Demo M-Series',     2.40, 3.20, '16 MB');

INSERT INTO graphic (gpu_id, graphic_brand, graphic_chip) VALUES
(1, 'Intel',  'Intel Demo UHD Graphics'),
(2, 'AMD',    'AMD Demo Radeon Vega'),
(3, 'NVIDIA', 'NVIDIA Demo GTX 1000'),
(4, 'NVIDIA', 'NVIDIA Demo RTX 2000'),
(5, 'NVIDIA', 'NVIDIA Demo RTX 4000'),
(6, 'Apple',  'Apple Demo GPU 8-Core');

INSERT INTO memory (memory_id, ram, ram_type) VALUES
(1, 4,  'DDR4'),
(2, 8,  'DDR4'),
(3, 16, 'DDR5'),
(4, 32, 'DDR5'),
(5, 8,  'Unified Memory'),
(6, 16, 'Unified Memory');

INSERT INTO storage (storage_id, hdd_type, hdd_capacity) VALUES
(1, 'eMMC',    '128 GB'),
(2, 'SSD M.2', '256 GB'),
(3, 'SSD M.2', '512 GB'),
(4, 'SSD M.2', '1 TB');

INSERT INTO display (display_id, display_size, display_specs, display_type, touchscreen) VALUES
(1, 14.0, '1366 x 768',  'HD LED',                'ไม่มี'),
(2, 15.6, '1920 x 1080', 'Full HD IPS',           'ไม่มี'),
(3, 15.6, '1920 x 1080', 'Full HD IPS 144Hz',     'ไม่มี'),
(4, 13.3, '2560 x 1600', 'Retina IPS',            'ไม่มี'),
(5, 14.0, '1920 x 1080', 'Full HD IPS Touch',     'มี'),
(6, 16.0, '2560 x 1440', 'QHD IPS 165Hz',         'ไม่มี');

INSERT INTO `connection` (connection_id, wifi, bluetooth) VALUES
(1, 'Wi-Fi 5 (802.11ac)', 'Bluetooth 4.2'),
(2, 'Wi-Fi 6 (802.11ax)', 'Bluetooth 5.1'),
(3, 'Wi-Fi 6E',           'Bluetooth 5.3');

INSERT INTO laptop_store (store_id, store_name, url_buy) VALUES
(1, 'logo_buy/Example_Store.svg', 'https://example.com/store/demo-laptop');

-- ------------------------------------------------------------
-- Laptops (สมมติทั้งหมด) — หนึ่งเครื่องต่อหนึ่ง Rule
-- Rule 1-5  : งบประมาณระดับ 1   Rule 6-9   : งบประมาณระดับ 2
-- Rule 10-13: งบประมาณระดับ 3   Rule 14-17 : งบประมาณระดับ 4
-- Rule 18   : งบประมาณระดับ 5
-- ------------------------------------------------------------

INSERT INTO laptops
(laptop_id, brand, model, `rule`, os, description, img, battery, pros, cons, prices, web_camera, io_ports,
 processor_id, gpu_id, display_id, memory_id, connection_id, storage_id, store_id) VALUES

(1, 'Acer', 'Acer Demo Aspire D15', 'Rule: 1', 'Windows 11 Home',
 'แล็ปท็อปตัวอย่างสำหรับงานประสิทธิภาพสูงในงบประมาณเริ่มต้น เหมาะกับงานกราฟิกเบื้องต้นและเกมทั่วไป (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', '3 Cell',
 '.- ประสิทธิภาพคุ้มราคา.- ระบายความร้อนดี', '.- ตัวเครื่องค่อนข้างหนา',
 14990, 'HD Webcam', ',- 1 x USB Type-C ,- 2 x USB 3.2 ,- 1 x HDMI',
 5, 3, 3, 2, 2, 3, 1),

(2, 'Hp', 'Hp Demo Pavilion Touch D14', 'Rule: 2', 'Windows 11 Home',
 'แล็ปท็อปตัวอย่างหน้าจอสัมผัส เหมาะกับงานทั่วไปและการจดบันทึก (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', '3 Cell',
 '.- หน้าจอสัมผัสใช้งานสะดวก.- น้ำหนักเบา', '.- สเปกไม่เหมาะกับงานหนัก',
 13990, 'HD Webcam', ',- 1 x USB Type-C ,- 2 x USB 3.2 ,- 1 x HDMI',
 1, 1, 5, 2, 1, 2, 1),

(3, 'Apple', 'Apple Demo AirBook D13', 'Rule: 3', 'macOS',
 'แล็ปท็อปตัวอย่างระบบ macOS สำหรับงานทั่วไปในงบประมาณเริ่มต้น (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', 'Built-in',
 '.- แบตเตอรี่ใช้งานได้ยาวนาน.- เครื่องเงียบไม่มีพัดลม', '.- พอร์ตเชื่อมต่อน้อย',
 14900, 'FaceTime HD', ',- 2 x Thunderbolt / USB 4',
 7, 6, 4, 5, 2, 1, 1),

(4, 'Lenovo', 'Lenovo Demo IdeaBook D14', 'Rule: 4', 'Windows 11 Home',
 'แล็ปท็อปตัวอย่างจอปกติ (ไม่สัมผัส) สำหรับงานเอกสารและเรียนออนไลน์ (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', '2 Cell',
 '.- ราคาเข้าถึงง่าย.- คีย์บอร์ดพิมพ์สบาย', '.- จอความละเอียดพื้นฐาน',
 11990, 'HD 720p', ',- 2 x USB 3.2 ,- 1 x HDMI ,- 1 x SD Card',
 4, 2, 2, 1, 1, 2, 1),

(5, 'Asus', 'Asus Demo VivoStudy D14', 'Rule: 5', 'Windows 11 Home',
 'แล็ปท็อปตัวอย่างสำหรับงานพื้นฐาน เรียนออนไลน์ ท่องเว็บ ในงบประมาณประหยัด (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', '2 Cell',
 '.- น้ำหนักเบาพกพาง่าย.- ราคาประหยัด', '.- ไม่เหมาะกับงานประมวลผลหนัก',
 9990, 'VGA Webcam', ',- 1 x USB 2.0 ,- 1 x USB 3.2 ,- 1 x HDMI',
 1, 1, 1, 1, 1, 1, 1),

(6, 'Msi', 'MSI Demo Sword D15', 'Rule: 6', 'Windows 11 Home',
 'แล็ปท็อปตัวอย่างสายเกมและกราฟิกในงบประมาณระดับกลาง (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', '4 Cell',
 '.- การ์ดจอแยกเล่นเกมลื่น.- จอ 144Hz', '.- แบตเตอรี่หมดเร็วเมื่อเล่นเกม',
 23990, 'HD Webcam', ',- 1 x USB Type-C ,- 3 x USB 3.2 ,- 1 x HDMI',
 5, 4, 3, 3, 2, 3, 1),

(7, 'Dell', 'Dell Demo Inspire D15', 'Rule: 7', 'Windows 11 Home',
 'แล็ปท็อปตัวอย่างสำหรับงานตัดต่อรูปและวิดีโอเบื้องต้น (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', '4 Cell',
 '.- งานประกอบแข็งแรง.- สเปกสมดุลกับราคา', '.- ดีไซน์ค่อนข้างเรียบ',
 21990, 'FHD Webcam', ',- 1 x USB Type-C ,- 2 x USB 3.2 ,- 1 x HDMI',
 2, 2, 2, 3, 2, 3, 1),

(8, 'Acer', 'Acer Demo Swift D14', 'Rule: 8', 'Windows 11 Home',
 'แล็ปท็อปตัวอย่างระบบ Windows สำหรับงานทั่วไป น้ำหนักเบา (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', '3 Cell',
 '.- บางเบาพกพาสะดวก.- แบตเตอรี่ใช้ได้ทั้งวัน', '.- อัปเกรดฮาร์ดแวร์ไม่ได้',
 18990, 'HD Webcam', ',- 1 x USB Type-C ,- 2 x USB 3.2 ,- 1 x HDMI',
 2, 1, 2, 2, 2, 3, 1),

(9, 'Apple', 'Apple Demo AirBook D13 Plus', 'Rule: 9', 'macOS',
 'แล็ปท็อปตัวอย่างระบบ macOS งบประมาณระดับกลาง (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', 'Built-in',
 '.- จอ Retina คมชัด.- ตัวเครื่องพรีเมียม', '.- ราคาสูงกว่าสเปกใกล้เคียง',
 24900, 'FaceTime HD', ',- 2 x Thunderbolt / USB 4',
 7, 6, 4, 5, 2, 2, 1),

(10, 'Lenovo', 'Lenovo Demo Legion D16', 'Rule: 10', 'Windows 11 Home',
 'แล็ปท็อปตัวอย่างประสิทธิภาพสูง เล่นเกมและงาน 3D ได้ดี (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', '4 Cell',
 '.- จอ QHD 165Hz.- ระบบระบายความร้อนคู่', '.- น้ำหนักมาก',
 37990, 'FHD Webcam', ',- 1 x USB Type-C ,- 3 x USB 3.2 ,- 1 x HDMI 2.1',
 3, 5, 6, 3, 3, 4, 1),

(11, 'Msi', 'MSI Demo Modern D14', 'Rule: 11', 'Windows 11 Home',
 'แล็ปท็อปตัวอย่างระบบ Windows สายทำงานระดับกลาง-สูง (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', '3 Cell',
 '.- ตัวเครื่องบางเบา.- สเปกแรงพอสำหรับตัดต่อ', '.- ลำโพงเสียงเบา',
 27990, 'FHD Webcam', ',- 1 x USB Type-C ,- 2 x USB 3.2 ,- 1 x HDMI',
 3, 2, 2, 3, 2, 3, 1),

(12, 'Asus', 'Asus Demo ZenLite D14', 'Rule: 12', 'Windows 11 Home',
 'แล็ปท็อปตัวอย่างงานพื้นฐานแต่วัสดุพรีเมียม (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', '3 Cell',
 '.- วัสดุอะลูมิเนียม.- น้ำหนักเบามาก', '.- พอร์ตน้อย',
 25990, 'HD Webcam', ',- 1 x USB Type-C ,- 1 x USB 3.2 ,- 1 x HDMI',
 2, 1, 2, 2, 2, 3, 1),

(13, 'Apple', 'Apple Demo ProBook D14', 'Rule: 13', 'macOS',
 'แล็ปท็อปตัวอย่างระบบ macOS สำหรับสายครีเอทีฟ (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', 'Built-in',
 '.- ประมวลผลวิดีโอเร็ว.- จอสีตรง', '.- ราคาสูง',
 39900, 'FaceTime HD', ',- 3 x Thunderbolt / USB 4 ,- 1 x HDMI',
 7, 6, 4, 6, 3, 3, 1),

(14, 'Dell', 'Dell Demo G-Force D16', 'Rule: 14', 'Windows 11 Pro',
 'แล็ปท็อปตัวอย่างประสิทธิภาพสูงสำหรับเกมและงานเรนเดอร์ (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', '6 Cell',
 '.- การ์ดจอระดับสูง.- อัปเกรดแรมได้', '.- อะแดปเตอร์ใหญ่',
 52990, 'FHD Webcam', ',- 1 x USB Type-C ,- 3 x USB 3.2 ,- 1 x HDMI 2.1',
 6, 5, 6, 4, 3, 4, 1),

(15, 'Hp', 'Hp Demo Envy D15', 'Rule: 15', 'Windows 11 Pro',
 'แล็ปท็อปตัวอย่างระบบ Windows ระดับพรีเมียมสำหรับสายทำงาน (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', '4 Cell',
 '.- งานประกอบพรีเมียม.- จอสีสวย', '.- ราคาสูง',
 45990, 'FHD IR Webcam', ',- 2 x USB Type-C ,- 2 x USB 3.2 ,- 1 x HDMI',
 3, 4, 2, 3, 3, 4, 1),

(16, 'Lenovo', 'Lenovo Demo ThinkLite D14', 'Rule: 16', 'Windows 11 Pro',
 'แล็ปท็อปตัวอย่างสายงานเอกสาร/ธุรกิจ เน้นความทนทาน (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', '3 Cell',
 '.- ผ่านมาตรฐานความทนทาน.- คีย์บอร์ดดีเยี่ยม', '.- ดีไซน์เรียบ',
 42990, 'FHD IR Webcam', ',- 2 x USB Type-C ,- 2 x USB 3.2 ,- 1 x HDMI',
 3, 1, 2, 3, 3, 3, 1),

(17, 'Apple', 'Apple Demo ProBook D16', 'Rule: 17', 'macOS',
 'แล็ปท็อปตัวอย่างระบบ macOS จอใหญ่สำหรับงานตัดต่อระดับจริงจัง (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', 'Built-in',
 '.- ประสิทธิภาพสูงมาก.- ลำโพงคุณภาพดี', '.- น้ำหนักมากกว่ารุ่นเล็ก',
 59900, 'FaceTime HD', ',- 3 x Thunderbolt / USB 4 ,- 1 x HDMI ,- 1 x SD Card',
 7, 6, 6, 6, 3, 4, 1),

(18, 'Msi', 'MSI Demo Titan D17', 'Rule: 18', 'Windows 11 Pro',
 'แล็ปท็อปตัวอย่างระดับท็อปสุดของกลุ่มตัวอย่าง สำหรับเกมและงาน 3D หนัก (ข้อมูลสมมติเพื่อการสาธิต)',
 'Laptop/placeholder.svg', '6 Cell',
 '.- สเปกสูงสุดในกลุ่มตัวอย่าง.- จอ QHD 165Hz', '.- ราคาสูงและน้ำหนักมาก',
 79990, 'FHD Webcam', ',- 2 x USB Type-C ,- 3 x USB 3.2 ,- 1 x HDMI 2.1',
 6, 5, 6, 4, 3, 4, 1);
