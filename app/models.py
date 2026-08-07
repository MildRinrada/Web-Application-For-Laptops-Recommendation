"""View models (dataclass) สำหรับส่งข้อมูลไปแสดงผลใน template

หมายเหตุ: ราคา (prices) ถูกจัดรูปแบบใส่เครื่องหมายคอมมาตั้งแต่ตอนสร้างอ็อบเจกต์
เพื่อให้ template แสดงผลได้เหมือนระบบเดิม
"""
from dataclasses import dataclass


def format_price(value):
    return "{:,}".format(value)


@dataclass
class LaptopSummary:
    """ข้อมูลย่อของแล็ปท็อป ใช้ในหน้ารายการ/ค้นหา/กรอง/แนะนำ

    price_value เก็บราคาเป็นตัวเลขสำหรับการกรองฝั่ง client
    ส่วน prices เป็นสตริงที่จัดรูปแบบแล้วสำหรับแสดงผล
    """

    laptop_id: int
    model: str
    cpu_model: str
    graphic_chip: str
    ram: int
    hdd_capacity: str
    prices: str
    img: str
    brand: str
    price_value: int

    @classmethod
    def from_row(cls, row):
        return cls(
            laptop_id=row[0],
            model=row[1],
            cpu_model=row[2],
            graphic_chip=row[3],
            ram=row[4],
            hdd_capacity=row[5],
            prices=format_price(row[6]),
            img=row[7],
            brand=row[8],
            price_value=row[6],
        )


@dataclass
class LaptopDetail:
    """ข้อมูลเต็มของแล็ปท็อป ใช้ในหน้ารายละเอียดและหน้าเปรียบเทียบ"""

    laptop_id: int
    brand: str
    model: str
    img: str
    wifi: str
    bluetooth: str
    web_camera: str
    description: str
    pros: str
    cons: str
    io_ports: str
    cpu_brand: str
    cpu_model: str
    base_clock: str
    boost_clock: str
    cache: str
    graphic_brand: str
    graphic_chip: str
    ram: int
    ram_type: str
    hdd_capacity: str
    hdd_type: str
    prices: str
    battery: str
    os: str
    store_name: str
    url_buy: str
    display_size: str
    display_specs: str
    display_type: str
    touchscreen: str

    @classmethod
    def from_row(cls, row):
        # ลำดับคอลัมน์ตรงกับ DETAIL_SELECT ใน repository.py
        return cls(
            laptop_id=row[0],
            brand=row[1],
            model=row[2],
            img=row[3],
            wifi=row[4],
            bluetooth=row[5],
            web_camera=row[6],
            description=row[7],
            pros=row[8],
            cons=row[9],
            io_ports=row[10],
            cpu_brand=row[11],
            cpu_model=row[12],
            base_clock=row[13],
            boost_clock=row[14],
            cache=row[15],
            graphic_brand=row[16],
            graphic_chip=row[17],
            ram=row[18],
            ram_type=row[19],
            hdd_capacity=row[20],
            hdd_type=row[21],
            prices=format_price(row[22]),
            battery=row[23],
            os=row[24],
            store_name=row[25],
            url_buy=row[26],
            display_size=row[27],
            display_specs=row[28],
            display_type=row[29],
            touchscreen=row[30],
        )

    # การตัดคำของ ข้อดี/ข้อเสีย/พอร์ต ใช้กติกาเดียวกับระบบเดิม
    @property
    def formatted_pros(self):
        return self.pros.split(".")

    @property
    def formatted_cons(self):
        return self.cons.split(".")

    @property
    def formatted_io(self):
        return self.io_ports.split(",")
