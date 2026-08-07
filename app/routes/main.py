"""หน้าหลัก ค้นหา รายละเอียด และเปรียบเทียบแล็ปท็อป"""
from flask import Blueprint, render_template, request

from .. import repository

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/search", methods=["GET", "POST"])
def search_laptop():
    if request.method == "POST":
        search_query = request.form["search_query"]
        laptops = repository.fetch_summaries(model_like=search_query)
        if laptops:
            return render_template("search_results.html", laptops=laptops)
    return render_template("search_notfound.html")


@main_bp.route("/laptop/<int:laptop_id>")
def laptop_information(laptop_id):
    laptop = repository.fetch_detail(laptop_id)
    if laptop is None:
        return "ไม่พบข้อมูลเครื่องคอมพิวเตอร์"
    return render_template("laptop_information.html", laptop=laptop)


@main_bp.route("/compare_laptop", methods=["POST"])
def compare_laptop():
    compare_ids = request.form.getlist("compare_laptop_ids")
    laptops = repository.fetch_details(compare_ids[:2])
    return render_template("compare_laptop.html", laptops=laptops)
