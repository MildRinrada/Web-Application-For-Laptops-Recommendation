-- ============================================================
-- Laptop Recommendation Web Application — Database Schema
-- ออกแบบใหม่จากการวิเคราะห์ Source Code เดิม (โครงสร้าง normalized)
-- MySQL 5.7+ / MariaDB 10.3+
--
-- หมายเหตุ:
-- - ใช้ collation แบบ case-insensitive (utf8mb4_unicode_ci)
--   เพื่อให้การเทียบค่า brand เช่น 'Msi' / 'MSI' ให้ผลเหมือนระบบเดิม
-- - คอลัมน์ `rule` เก็บผลของ Rule-based Expert System ในรูปแบบ 'Rule: N'
--   (N = 1-18) ตาม logic เดิมของระบบแนะนำ
-- ============================================================

CREATE DATABASE IF NOT EXISTS laptopdb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE laptopdb;

-- ------------------------------------------------------------
-- ตารางอ้างอิง (Lookup tables)
-- ------------------------------------------------------------

CREATE TABLE IF NOT EXISTS processor (
    processor_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    cpu_brand    VARCHAR(50)  NOT NULL,
    cpu_model    VARCHAR(100) NOT NULL,
    base_clock   DECIMAL(4,2) NULL,
    boost_clock  DECIMAL(4,2) NULL,
    cache        VARCHAR(50)  NULL,
    PRIMARY KEY (processor_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS graphic (
    gpu_id        INT UNSIGNED NOT NULL AUTO_INCREMENT,
    graphic_brand VARCHAR(50)  NOT NULL,
    graphic_chip  VARCHAR(100) NOT NULL,
    PRIMARY KEY (gpu_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS memory (
    memory_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ram       INT UNSIGNED NOT NULL,          -- หน่วย GB
    ram_type  VARCHAR(50)  NULL,
    PRIMARY KEY (memory_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS storage (
    storage_id   INT UNSIGNED NOT NULL AUTO_INCREMENT,
    hdd_type     VARCHAR(50) NULL,            -- เช่น 'SSD M.2'
    hdd_capacity VARCHAR(20) NOT NULL,        -- เช่น '512 GB', '1 TB' (ตรงกับตัวกรองบนหน้าเว็บ)
    PRIMARY KEY (storage_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS display (
    display_id    INT UNSIGNED NOT NULL AUTO_INCREMENT,
    display_size  DECIMAL(4,1) NULL,          -- นิ้ว
    display_specs VARCHAR(50)  NULL,          -- เช่น '1920 x 1080'
    display_type  VARCHAR(100) NULL,          -- เช่น 'Full HD IPS 144Hz'
    touchscreen   VARCHAR(20)  NULL,          -- 'มี' / 'ไม่มี'
    PRIMARY KEY (display_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `connection` (
    connection_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    wifi          VARCHAR(100) NULL,
    bluetooth     VARCHAR(50)  NULL,
    PRIMARY KEY (connection_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS laptop_store (
    store_id   INT UNSIGNED NOT NULL AUTO_INCREMENT,
    store_name VARCHAR(150) NOT NULL,         -- path โลโก้ร้านค้าใน static/ เช่น 'logo_buy/Example_Store.svg'
    url_buy    VARCHAR(500) NULL,
    PRIMARY KEY (store_id)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- ตารางหลัก
-- ------------------------------------------------------------

CREATE TABLE IF NOT EXISTS laptops (
    laptop_id     INT UNSIGNED NOT NULL AUTO_INCREMENT,
    brand         VARCHAR(50)  NOT NULL,      -- Acer / Apple / Asus / Dell / Hp / Lenovo / Msi
    model         VARCHAR(150) NOT NULL,
    `rule`        VARCHAR(20)  NULL,          -- 'Rule: 1' ... 'Rule: 18' (ผลจาก Rule-based System)
    os            VARCHAR(50)  NULL,
    description   TEXT         NULL,
    img           VARCHAR(255) NULL,          -- path รูปภาพใน static/
    battery       VARCHAR(50)  NULL,
    pros          TEXT         NULL,          -- ข้อดี คั่นแต่ละข้อด้วย '.'
    cons          TEXT         NULL,          -- ข้อเสีย คั่นแต่ละข้อด้วย '.'
    prices        INT UNSIGNED NOT NULL,      -- ราคา (บาท)
    web_camera    VARCHAR(100) NULL,
    io_ports      TEXT         NULL,          -- พอร์ต คั่นแต่ละรายการด้วย ','
    processor_id  INT UNSIGNED NOT NULL,
    gpu_id        INT UNSIGNED NOT NULL,
    display_id    INT UNSIGNED NOT NULL,
    memory_id     INT UNSIGNED NOT NULL,
    connection_id INT UNSIGNED NOT NULL,
    storage_id    INT UNSIGNED NOT NULL,
    store_id      INT UNSIGNED NOT NULL,
    PRIMARY KEY (laptop_id),
    CONSTRAINT fk_laptops_processor  FOREIGN KEY (processor_id)  REFERENCES processor (processor_id),
    CONSTRAINT fk_laptops_graphic    FOREIGN KEY (gpu_id)        REFERENCES graphic (gpu_id),
    CONSTRAINT fk_laptops_display    FOREIGN KEY (display_id)    REFERENCES display (display_id),
    CONSTRAINT fk_laptops_memory     FOREIGN KEY (memory_id)     REFERENCES memory (memory_id),
    CONSTRAINT fk_laptops_connection FOREIGN KEY (connection_id) REFERENCES `connection` (connection_id),
    CONSTRAINT fk_laptops_storage    FOREIGN KEY (storage_id)    REFERENCES storage (storage_id),
    CONSTRAINT fk_laptops_store      FOREIGN KEY (store_id)      REFERENCES laptop_store (store_id),
    INDEX idx_laptops_brand  (brand),
    INDEX idx_laptops_prices (prices),
    INDEX idx_laptops_rule   (`rule`),
    INDEX idx_laptops_model  (model)
) ENGINE=InnoDB;
