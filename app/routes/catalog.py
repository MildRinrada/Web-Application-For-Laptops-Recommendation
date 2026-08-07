"""หน้ารายการแล็ปท็อปตามยี่ห้อ และการเรียงลำดับราคา

URL ของหน้ารายการคงรูปแบบเดิมของระบบไว้ (เช่น /Acer_list, /sort_laptops_acer)
แต่ยุบ handler ที่ซ้ำกันต่อแบรนด์ให้เหลือ handler เดียวที่รับชื่อแบรนด์
เป็นพารามิเตอร์

หมายเหตุ: การกรองข้อมูล (ยี่ห้อ/ราคา/RAM/ความจุ) เป็นแบบ realtime ฝั่ง client
ใน templates/components/filter_panel.html — กรองเฉพาะรายการที่แสดงบนหน้านั้น
จึงไม่มี endpoint สำหรับกรองฝั่ง server อีกต่อไป
"""
from flask import Blueprint, render_template, request

from .. import repository

catalog_bp = Blueprint("catalog", __name__)

# ค่า brand ในฐานข้อมูล
BRANDS = ["Acer", "Apple", "Asus", "Dell", "Hp", "Lenovo", "Msi"]

# ชื่อที่ใช้แสดงผลบนหน้าเว็บ (คงตามหน้าเดิม)
BRAND_DISPLAY = {"Msi": "MSI"}

# URL ของฟอร์มเรียงราคาในระบบเดิมใช้ชื่อแบรนด์ตัวพิมพ์เล็ก
SORT_SLUG_TO_BRAND = {brand.lower(): brand for brand in BRANDS}

SORT_ORDER = {"lowsort": "asc", "expensivesort": "desc"}  # 'start' = ไม่เรียง


def render_brand_list(brand, laptops):
    return render_template(
        "brand_list.html",
        brand=brand,
        brand_display=BRAND_DISPLAY.get(brand, brand),
        laptops=laptops,
    )


@catalog_bp.route("/<any(Acer, Apple, Asus, Dell, Hp, Lenovo, Msi):brand>_list")
def brand_list(brand):
    laptops = repository.fetch_summaries(brand=brand)
    return render_brand_list(brand, laptops)


@catalog_bp.route(
    "/sort_laptops_<any(search, acer, apple, asus, dell, hp, lenovo, msi):target>",
    methods=["POST"],
)
def sort_laptops(target):
    order = SORT_ORDER.get(request.form["sort"])
    if target == "search":
        laptops = repository.fetch_summaries(order_by_price=order)
        return render_template("search_results.html", laptops=laptops)
    brand = SORT_SLUG_TO_BRAND[target]
    laptops = repository.fetch_summaries(brand=brand, order_by_price=order)
    return render_brand_list(brand, laptops)
