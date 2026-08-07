"""ชั้นเข้าถึงข้อมูล (Data Access Layer)

รวม SQL ทั้งหมดไว้ที่เดียว แทนที่ฟังก์ชันซ้ำ ๆ ต่อแบรนด์/ต่อเงื่อนไขในระบบเดิม
ทุก query ใช้ parameter binding เพื่อป้องกัน SQL injection
"""
from sqlalchemy import bindparam, text

from .extensions import db
from .models import LaptopDetail, LaptopSummary

# คอลัมน์และการ join ชุดเดียวกับ query เดิมทุกตัว (หน้ารายการ)
SUMMARY_SELECT = """
    SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram,
           s2.hdd_capacity, l.prices, l.img
    FROM laptops l
    JOIN processor p ON l.processor_id = p.processor_id
    JOIN graphic g   ON l.gpu_id       = g.gpu_id
    JOIN memory m    ON l.memory_id    = m.memory_id
    JOIN storage s2  ON l.storage_id   = s2.storage_id
"""

# คอลัมน์ชุดเดียวกับหน้ารายละเอียด/เปรียบเทียบของระบบเดิม (เพิ่ม laptop_id)
DETAIL_SELECT = """
    SELECT l.laptop_id, l.brand, l.model, l.img, c.wifi, c.bluetooth,
           l.web_camera, l.description, l.pros, l.cons, l.io_ports,
           p.cpu_brand, p.cpu_model, p.base_clock, p.boost_clock, p.cache,
           g.graphic_brand, g.graphic_chip, m.ram, m.ram_type,
           s2.hdd_capacity, s2.hdd_type, l.prices, l.battery, l.os,
           s.store_name, s.url_buy,
           d.display_size, d.display_specs, d.display_type, d.touchscreen
    FROM laptops l
    JOIN processor p     ON l.processor_id  = p.processor_id
    JOIN graphic g       ON l.gpu_id        = g.gpu_id
    JOIN memory m        ON l.memory_id     = m.memory_id
    JOIN storage s2      ON l.storage_id    = s2.storage_id
    JOIN display d       ON l.display_id    = d.display_id
    JOIN `connection` c  ON l.connection_id = c.connection_id
    JOIN laptop_store s  ON l.store_id      = s.store_id
"""


def fetch_summaries(
    brand=None,
    brands=None,
    rams=None,
    hdd_capacities=None,
    min_price=None,
    max_price=None,
    rule=None,
    model_like=None,
    order_by_price=None,
):
    """ดึงรายการแล็ปท็อปตามเงื่อนไขที่เลือก (เงื่อนไขไหนไม่ส่งมาก็ไม่กรอง)"""
    conditions = []
    params = {}
    expanding = []

    if brand:
        conditions.append("l.brand = :brand")
        params["brand"] = brand
    if brands:
        conditions.append("l.brand IN :brands")
        params["brands"] = list(brands)
        expanding.append("brands")
    if rams:
        conditions.append("m.ram IN :rams")
        params["rams"] = list(rams)
        expanding.append("rams")
    if hdd_capacities:
        conditions.append("s2.hdd_capacity IN :hdd_capacities")
        params["hdd_capacities"] = list(hdd_capacities)
        expanding.append("hdd_capacities")
    if min_price is not None and max_price is not None:
        conditions.append("l.prices BETWEEN :min_price AND :max_price")
        params["min_price"] = min_price
        params["max_price"] = max_price
    if rule:
        conditions.append("l.rule = :rule")
        params["rule"] = rule
    if model_like:
        conditions.append("l.model LIKE :model_like")
        params["model_like"] = f"%{model_like}%"

    sql = SUMMARY_SELECT
    if conditions:
        sql += " WHERE " + " AND ".join(conditions)
    if order_by_price in ("asc", "desc"):
        sql += f" ORDER BY l.prices {order_by_price.upper()}"

    stmt = text(sql)
    for name in expanding:
        stmt = stmt.bindparams(bindparam(name, expanding=True))

    rows = db.session.execute(stmt, params)
    return [LaptopSummary.from_row(row) for row in rows]


def fetch_detail(laptop_id):
    """ดึงข้อมูลเต็มของแล็ปท็อปหนึ่งเครื่อง (ไม่พบคืนค่า None)"""
    stmt = text(DETAIL_SELECT + " WHERE l.laptop_id = :laptop_id")
    row = db.session.execute(stmt, {"laptop_id": laptop_id}).fetchone()
    return LaptopDetail.from_row(row) if row else None


def fetch_details(laptop_ids):
    """ดึงข้อมูลเต็มของแล็ปท็อปหลายเครื่อง ใช้ในหน้าเปรียบเทียบ"""
    if not laptop_ids:
        return []
    stmt = text(DETAIL_SELECT + " WHERE l.laptop_id IN :laptop_ids").bindparams(
        bindparam("laptop_ids", expanding=True)
    )
    rows = db.session.execute(stmt, {"laptop_ids": list(laptop_ids)})
    return [LaptopDetail.from_row(row) for row in rows]
