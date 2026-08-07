"""ระบบแนะนำแล็ปท็อปแบบ Rule-based

ผู้ใช้ตอบคำถามทีละขั้น (งบประมาณ → การใช้งาน → ระบบปฏิบัติการ → หน้าจอสัมผัส)
แต่ละเส้นทางจบที่ rule หมายเลข 1-18 ซึ่งจับคู่กับคอลัมน์ `rule` ในฐานข้อมูล

โครงสร้างคำถาม (STEPS) ถอดมาจากหน้า recom/*.html เดิมทั้ง 9 หน้าแบบไม่เปลี่ยน
เส้นทางการตัดสินใจใด ๆ — เปลี่ยนเฉพาะวิธี render ให้ใช้ template เดียว
"""
import re

from flask import Blueprint, render_template, request

from .. import repository

recommendation_bp = Blueprint("recommendation", __name__)

# คำอธิบายใต้ตัวเลือก "การใช้งานที่ต้องการ" (ใช้ซ้ำทุกระดับงบประมาณ)
USAGE_DESCRIPTIONS = [
    "เหมาะกับงานพื้นฐาน เช่น การเรียนออนไลน์<br>\n"
    "ท่องเว็บ การใช้งาน Microsoft Words<br>\n"
    "มักมีราคาถูกและน้ำหนักเบาว่า<br>\n"
    "แต่ไม่สามารถใช้งานประมวลผลหนัก",
    "เหมาะสำหรับงานที่มีความซับซ้อนกว่างานทั่วไปแต่ไม่<br>\n"
    "ได้ต้องการการประมวลผลที่มากเกินไป เช่น <br>\n"
    "การตัดต่อรูป ทำตัดต่อคลิปวิดีโอ เล่นเกม the <br>\n"
    "sims 4, stardew valley",
    "เหมาะสำหรับงานที่เน้นประสิทธิภาพสูง<br>\n"
    "สุดเช่น Adobe Creative Cloud<br>\n"
    "มักมีราคาที่สูงกว่าและมีน้ำหนักมากกว่า",
]

# ตัวเลือกแต่ละขั้น: to=('rule', 'ruleN') ไปหน้าผลลัพธ์, to=('step', ชื่อขั้น) ไปคำถามถัดไป
STEPS = {
    "spec1": {
        "question": "การใช้งานที่ต้องการ",
        "grid": "gridthree",
        "img_width": 200,
        "options": [
            {"img": "recommendation/1_spec.png", "to": ("rule", "rule5")},
            {"img": "recommendation/2_spec.png", "to": ("step", "spec_medium_os1")},
            {"img": "recommendation/3_spec.png", "to": ("rule", "rule1")},
        ],
        "descriptions": USAGE_DESCRIPTIONS,
    },
    "spec_medium_os1": {
        "question": "ระบบปฎิบัติการที่ต้องการ",
        "grid": "gridtwo",
        "img_width": 250,
        "options": [
            {"img": "recommendation/1_os.png", "to": ("step", "spec_medium_os_touch1")},
            {"img": "recommendation/4_os.png", "to": ("rule", "rule3")},
        ],
    },
    "spec_medium_os_touch1": {
        "question": "ต้องการแล็ปท็อปที่มีหน้าจอสัมผัสหรือไม่",
        "grid": "gridtwo",
        "img_width": 250,
        "options": [
            {"img": "recommendation/1_touch.png", "to": ("rule", "rule2")},
            {"img": "recommendation/2_touch.png", "to": ("rule", "rule4")},
        ],
    },
    "spec2": {
        "question": "การใช้งานที่ต้องการ",
        "grid": "gridthree",
        "img_width": 200,
        "options": [
            {"img": "recommendation/1_spec.png", "to": ("step", "spec_low_os2")},
            {"img": "recommendation/2_spec.png", "to": ("rule", "rule7")},
            {"img": "recommendation/3_spec.png", "to": ("rule", "rule6")},
        ],
        "descriptions": USAGE_DESCRIPTIONS,
    },
    "spec_low_os2": {
        "question": "ระบบปฎิบัติการที่ต้องการ",
        "grid": "gridtwo",
        "img_width": 250,
        "options": [
            {"img": "recommendation/1_os.png", "to": ("rule", "rule8")},
            {"img": "recommendation/2_os.png", "to": ("rule", "rule9")},
        ],
    },
    "spec3": {
        "question": "การใช้งานที่ต้องการ",
        "grid": "gridthree",
        "img_width": 200,
        "options": [
            {"img": "recommendation/1_spec.png", "to": ("rule", "rule12")},
            {"img": "recommendation/2_spec.png", "to": ("step", "spec_medium_os3")},
            {"img": "recommendation/3_spec.png", "to": ("rule", "rule10")},
        ],
        "descriptions": USAGE_DESCRIPTIONS,
    },
    "spec_medium_os3": {
        "question": "ระบบปฎิบัติการที่ต้องการ",
        "grid": "gridtwo",
        "img_width": 250,
        "options": [
            {"img": "recommendation/1_os.png", "to": ("rule", "rule11")},
            {"img": "recommendation/3_os.png", "to": ("rule", "rule13")},
        ],
    },
    "spec4": {
        "question": "การใช้งานที่ต้องการ",
        "grid": "gridthree",
        "img_width": 200,
        "options": [
            {"img": "recommendation/1_spec.png", "to": ("rule", "rule16")},
            {"img": "recommendation/2_spec.png", "to": ("step", "spec_medium_os4")},
            {"img": "recommendation/3_spec.png", "to": ("rule", "rule14")},
        ],
        "descriptions": USAGE_DESCRIPTIONS,
    },
    "spec_medium_os4": {
        "question": "ระบบปฎิบัติการที่ต้องการ",
        "grid": "gridtwo",
        "img_width": 250,
        "options": [
            {"img": "recommendation/1_os.png", "to": ("rule", "rule15")},
            {"img": "recommendation/3_os.png", "to": ("rule", "rule17")},
        ],
    },
}

STEP_SLUGS = ", ".join(STEPS)


@recommendation_bp.route("/recommendation")
def recommendation():
    return render_template("recommendation.html")


@recommendation_bp.route(
    f"/recommendation_<any({STEP_SLUGS}):step>", endpoint="recommendation_step"
)
def recommendation_step(step):
    return render_template("recom_step.html", step_key=step, step=STEPS[step])


@recommendation_bp.route("/recommendation_list")
def recommendation_list():
    rule = request.args.get("rule", "")
    laptops = []
    match = re.fullmatch(r"rule(\d+)", rule)
    if match and 1 <= int(match.group(1)) <= 18:
        laptops = repository.fetch_summaries(rule=f"Rule: {match.group(1)}")
    return render_template("recommendation_list.html", laptops=laptops)
