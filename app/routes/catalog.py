"""หน้ารายการแล็ปท็อปตามยี่ห้อ การกรอง และการเรียงลำดับราคา

URL ทั้งหมดคงรูปแบบเดิมของระบบไว้ (เช่น /Acer_list, /sort_laptops_acer,
/filter_laptops_by_ram_Lenovo) แต่ยุบ handler ที่ซ้ำกันต่อแบรนด์
ให้เหลือ handler เดียวที่รับชื่อแบรนด์เป็นพารามิเตอร์
"""
from flask import Blueprint, render_template, request

from .. import repository

catalog_bp = Blueprint("catalog", __name__)

# ค่า brand ในฐานข้อมูล
BRANDS = ["Acer", "Apple", "Asus", "Dell", "Hp", "Lenovo", "Msi"]

# ชื่อที่ใช้แสดงผลบนหน้าเว็บ (คงตามหน้าเดิม)
BRAND_DISPLAY = {"Msi": "MSI"}

# URL ของฟอร์มกรองรายแบรนด์ในระบบเดิมใช้ "MSI" ตัวพิมพ์ใหญ่
FILTER_SLUG_TO_BRAND = {
    "Lenovo": "Lenovo", "Acer": "Acer", "MSI": "Msi", "Asus": "Asus",
    "Dell": "Dell", "Hp": "Hp", "Apple": "Apple",
}
BRAND_TO_FILTER_SLUG = {brand: slug for slug, brand in FILTER_SLUG_TO_BRAND.items()}

# URL ของฟอร์มเรียงราคาในระบบเดิมใช้ชื่อแบรนด์ตัวพิมพ์เล็ก
SORT_SLUG_TO_BRAND = {brand.lower(): brand for brand in BRANDS}

SORT_ORDER = {"lowsort": "asc", "expensivesort": "desc"}  # 'start' = ไม่เรียง


def render_brand_list(brand, laptops):
    return render_template(
        "brand_list.html",
        brand=brand,
        brand_display=BRAND_DISPLAY.get(brand, brand),
        filter_slug=BRAND_TO_FILTER_SLUG[brand],
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


@catalog_bp.route("/filter_laptops", methods=["POST"])
def filter_laptops():
    selected_brands = request.form.getlist("brand")
    laptops = repository.fetch_summaries(brands=selected_brands)
    return render_template("filtered_laptops.html", laptops=laptops)


def _brand_filter_response(brand, laptops):
    """ผลการกรองรายแบรนด์: ถ้าไม่พบข้อมูลแสดงหน้า notfound (พฤติกรรมเดิม)"""
    if not laptops:
        return render_template("search_notfound.html")
    return render_brand_list(brand, laptops)


@catalog_bp.route("/filter_laptops_by_ram", methods=["POST"], defaults={"brand_slug": None})
@catalog_bp.route(
    "/filter_laptops_by_ram_<any(Lenovo, Acer, MSI, Asus, Dell, Hp, Apple):brand_slug>",
    methods=["POST"],
)
def filter_laptops_by_ram(brand_slug):
    selected_ram = request.form.getlist("ram")
    if brand_slug is None:
        laptops = repository.fetch_summaries(rams=selected_ram)
        return render_template("filtered_laptops.html", laptops=laptops)
    brand = FILTER_SLUG_TO_BRAND[brand_slug]
    laptops = repository.fetch_summaries(brand=brand, rams=selected_ram)
    return _brand_filter_response(brand, laptops)


@catalog_bp.route("/filter_laptops_by_hdd", methods=["POST"], defaults={"brand_slug": None})
@catalog_bp.route(
    "/filter_laptops_by_hdd_<any(Lenovo, Acer, MSI, Asus, Dell, Hp, Apple):brand_slug>",
    methods=["POST"],
)
def filter_laptops_by_hdd(brand_slug):
    selected_hdd = request.form.getlist("hdd_capacity")
    if brand_slug is None:
        laptops = repository.fetch_summaries(hdd_capacities=selected_hdd)
        return render_template("filtered_laptops.html", laptops=laptops)
    brand = FILTER_SLUG_TO_BRAND[brand_slug]
    laptops = repository.fetch_summaries(brand=brand, hdd_capacities=selected_hdd)
    return _brand_filter_response(brand, laptops)


@catalog_bp.route("/filter_laptops_by_price", methods=["POST"], defaults={"brand_slug": None})
@catalog_bp.route(
    "/filter_laptops_by_price_<any(Lenovo, Acer, MSI, Asus, Dell, Hp, Apple):brand_slug>",
    methods=["POST"],
)
def filter_laptops_by_price(brand_slug):
    min_price = request.form["min_price"]
    max_price = request.form["max_price"]
    brand = FILTER_SLUG_TO_BRAND.get(brand_slug)
    laptops = repository.fetch_summaries(
        brand=brand, min_price=min_price, max_price=max_price
    )
    if not laptops:
        return render_template("search_notfound.html")
    if brand is None:
        return render_template("filtered_laptops.html", laptops=laptops)
    return render_brand_list(brand, laptops)
