"""หน้าแสดงข้อผิดพลาดของระบบ (ธีมเดียวกับเว็บไซต์)"""
from flask import render_template

ERROR_PAGES = {
    404: {
        "error_title": "ไม่พบหน้าที่คุณต้องการ",
        "error_message": "หน้าที่คุณเรียกอาจถูกย้าย ถูกลบ หรือพิมพ์ URL ไม่ถูกต้อง "
                         "กรุณาตรวจสอบลิงก์อีกครั้ง หรือกลับไปเริ่มต้นที่หน้าหลัก",
    },
    405: {
        "error_title": "วิธีการเรียกใช้งานไม่ถูกต้อง",
        "error_message": "หน้านี้ไม่รองรับวิธีการเรียกใช้งานที่ส่งมา "
                         "กรุณากลับไปใช้งานผ่านหน้าเว็บตามปกติ",
    },
    500: {
        "error_title": "เกิดข้อผิดพลาดภายในระบบ",
        "error_message": "ระบบขัดข้องชั่วคราว กรุณาลองใหม่อีกครั้งภายหลัง "
                         "หากยังพบปัญหาอยู่ กรุณาติดต่อผู้ดูแลระบบ",
    },
}


def register_error_handlers(app):
    def render_error_page(code):
        def handler(error):
            return render_template("error.html", code=code, **ERROR_PAGES[code]), code
        return handler

    for code in ERROR_PAGES:
        app.register_error_handler(code, render_error_page(code))
