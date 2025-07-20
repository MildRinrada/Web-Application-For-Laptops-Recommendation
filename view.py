from flask import Flask, render_template, request
from models import Laptop1, Laptop2, Laptop3
from app import app, db
from sqlalchemy import text

class Laptops(db.Model):
    laptop_id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    prices = db.Column(db.Integer, nullable=False)  
    hdd_capacity = db.Column(db.String(50))
    ram = db.Column(db.Integer)
    graphic_chip = db.Column(db.String(50))
    cpu_model = db.Column(db.String(50))
    img = db.Column(db.String(100))
    
    @staticmethod
    def filter_laptop_by_brand(brands):
        connection = Laptop1.connector()
        cursor = connection.cursor()

        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        brand_placeholders = ", ".join(["%s"] * len(brands))
        
        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแบรนด์
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE l.brand IN ({brand_placeholders}) 
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(brands))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list

    @staticmethod
    def filter_laptop_by_ram(ram):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        ram_placeholders = ", ".join(["%s"] * len(ram))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE m.ram IN ({ram_placeholders}) 
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(ram))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list

    @staticmethod
    def filter_laptop_by_ram_Lenovo(ram):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        ram_placeholders = ", ".join(["%s"] * len(ram))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE m.ram IN ({ram_placeholders}) AND l.brand = 'Lenovo'
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(ram))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list
    
    @staticmethod
    def filter_laptop_by_ram_Acer(ram):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        ram_placeholders = ", ".join(["%s"] * len(ram))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE m.ram IN ({ram_placeholders}) AND l.brand = 'Acer'
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(ram))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list
    
    @staticmethod
    def filter_laptop_by_ram_MSI(ram):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        ram_placeholders = ", ".join(["%s"] * len(ram))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE m.ram IN ({ram_placeholders}) AND l.brand = 'MSI'
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(ram))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list
    
    @staticmethod
    def filter_laptop_by_ram_Asus(ram):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        ram_placeholders = ", ".join(["%s"] * len(ram))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE m.ram IN ({ram_placeholders}) AND l.brand = 'Asus'
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(ram))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list
    
    @staticmethod
    def filter_laptop_by_ram_Dell(ram):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        ram_placeholders = ", ".join(["%s"] * len(ram))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE m.ram IN ({ram_placeholders}) AND l.brand = 'Dell'
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(ram))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list

    @staticmethod
    def filter_laptop_by_ram_Hp(ram):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        ram_placeholders = ", ".join(["%s"] * len(ram))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE m.ram IN ({ram_placeholders}) AND l.brand = 'Hp'
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(ram))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list
    
    @staticmethod
    def filter_laptop_by_ram_Apple(ram):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        ram_placeholders = ", ".join(["%s"] * len(ram))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE m.ram IN ({ram_placeholders}) AND l.brand = 'Apple'
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(ram))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list
        
    @staticmethod
    def filter_laptop_by_hdd(hdd_capacity):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        hdd_capacity_placeholders = ", ".join(["%s"] * len(hdd_capacity))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE s2.hdd_capacity IN ({hdd_capacity_placeholders}) 
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(hdd_capacity))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list
    
    @staticmethod
    def filter_laptop_by_hdd_Lenovo(hdd_capacity):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        hdd_capacity_placeholders = ", ".join(["%s"] * len(hdd_capacity))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE s2.hdd_capacity IN ({hdd_capacity_placeholders}) AND l.brand = 'Lenovo'
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(hdd_capacity))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list  
    
    @staticmethod
    def filter_laptop_by_hdd_Asus(hdd_capacity):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        hdd_capacity_placeholders = ", ".join(["%s"] * len(hdd_capacity))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE s2.hdd_capacity IN ({hdd_capacity_placeholders}) AND l.brand = 'Asus'
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(hdd_capacity))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list   
    
    @staticmethod
    def filter_laptop_by_hdd_MSI(hdd_capacity):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        hdd_capacity_placeholders = ", ".join(["%s"] * len(hdd_capacity))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE s2.hdd_capacity IN ({hdd_capacity_placeholders}) AND l.brand = 'MSI'
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(hdd_capacity))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list    
    
    @staticmethod
    def filter_laptop_by_hdd_Acer(hdd_capacity):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        hdd_capacity_placeholders = ", ".join(["%s"] * len(hdd_capacity))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE s2.hdd_capacity IN ({hdd_capacity_placeholders}) AND l.brand = 'Acer'
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(hdd_capacity))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list   
    
    @staticmethod
    def filter_laptop_by_hdd_Dell(hdd_capacity):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        hdd_capacity_placeholders = ", ".join(["%s"] * len(hdd_capacity))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE s2.hdd_capacity IN ({hdd_capacity_placeholders}) AND l.brand = 'Dell'
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(hdd_capacity))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list     

    @staticmethod
    def filter_laptop_by_hdd_Hp(hdd_capacity):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        hdd_capacity_placeholders = ", ".join(["%s"] * len(hdd_capacity))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE s2.hdd_capacity IN ({hdd_capacity_placeholders}) AND l.brand = 'Hp'
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(hdd_capacity))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list    
    
    @staticmethod
    def filter_laptop_by_hdd_Apple(hdd_capacity):
        connection = Laptop1.connector()
        cursor = connection.cursor()
        
        # สร้างสตริงสำหรับใช้ในการระบุแต่ละค่าในพารามิเตอร์
        hdd_capacity_placeholders = ", ".join(["%s"] * len(hdd_capacity))

        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูลตามแรม
        query = f"""
        SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
        FROM laptops l, graphic g, memory m, processor p, storage s2 
        WHERE s2.hdd_capacity IN ({hdd_capacity_placeholders}) AND l.brand = 'Apple'
        AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """

        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, tuple(hdd_capacity))

        result = cursor.fetchall()
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list           
    
    @staticmethod
    def filter_laptops_by_price(min_price, max_price):
        # สร้าง SQL query เพื่อดึงข้อมูลเครื่องโน้ตบุ๊กที่มีราคาอยู่ในช่วงที่ระบุ
        query = text("""
            SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
            FROM laptops l, graphic g, memory m, processor p, storage s2 
            WHERE prices BETWEEN :min_price AND :max_price AND l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id
        """)
        # ทำการ execute SQL query ด้วย SQLAlchemy
        result = db.session.execute(query, {'min_price': min_price, 'max_price': max_price})
        
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list
    
    @staticmethod
    def filter_laptops_by_price_Lenovo(min_price, max_price):
        query = text("""
            SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
            FROM laptops l, graphic g, memory m, processor p, storage s2 
            WHERE prices BETWEEN :min_price AND :max_price AND l.brand = 'Lenovo' AND l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id
        """)
        result = db.session.execute(query, {'min_price': min_price, 'max_price': max_price})
        
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list
    
    @staticmethod
    def filter_laptops_by_price_Acer(min_price, max_price):
        # สร้าง SQL query เพื่อดึงข้อมูลเครื่องโน้ตบุ๊กที่มีราคาอยู่ในช่วงที่ระบุ
        query = text("""
            SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
            FROM laptops l, graphic g, memory m, processor p, storage s2 
            WHERE prices BETWEEN :min_price AND :max_price AND l.brand = 'Acer' AND l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id
        """)
        # ทำการ execute SQL query ด้วย SQLAlchemy
        result = db.session.execute(query, {'min_price': min_price, 'max_price': max_price})
        
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list
    
    @staticmethod
    def filter_laptops_by_price_MSI(min_price, max_price):
        # สร้าง SQL query เพื่อดึงข้อมูลเครื่องโน้ตบุ๊กที่มีราคาอยู่ในช่วงที่ระบุ
        query = text("""
            SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
            FROM laptops l, graphic g, memory m, processor p, storage s2 
            WHERE prices BETWEEN :min_price AND :max_price AND l.brand = 'MSI' AND l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id
        """)
        # ทำการ execute SQL query ด้วย SQLAlchemy
        result = db.session.execute(query, {'min_price': min_price, 'max_price': max_price})
        
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list  
    
    @staticmethod
    def filter_laptops_by_price_Asus(min_price, max_price):
        # สร้าง SQL query เพื่อดึงข้อมูลเครื่องโน้ตบุ๊กที่มีราคาอยู่ในช่วงที่ระบุ
        query = text("""
            SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
            FROM laptops l, graphic g, memory m, processor p, storage s2 
            WHERE prices BETWEEN :min_price AND :max_price AND l.brand = 'Asus' AND l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id
        """)
        # ทำการ execute SQL query ด้วย SQLAlchemy
        result = db.session.execute(query, {'min_price': min_price, 'max_price': max_price})
        
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list    
    
    @staticmethod
    def filter_laptops_by_price_Dell(min_price, max_price):
        # สร้าง SQL query เพื่อดึงข้อมูลเครื่องโน้ตบุ๊กที่มีราคาอยู่ในช่วงที่ระบุ
        query = text("""
            SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
            FROM laptops l, graphic g, memory m, processor p, storage s2 
            WHERE prices BETWEEN :min_price AND :max_price AND l.brand = 'Dell' AND l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id
        """)
        # ทำการ execute SQL query ด้วย SQLAlchemy
        result = db.session.execute(query, {'min_price': min_price, 'max_price': max_price})
        
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list   
    
    @staticmethod
    def filter_laptops_by_price_Hp(min_price, max_price):
        # สร้าง SQL query เพื่อดึงข้อมูลเครื่องโน้ตบุ๊กที่มีราคาอยู่ในช่วงที่ระบุ
        query = text("""
            SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
            FROM laptops l, graphic g, memory m, processor p, storage s2 
            WHERE prices BETWEEN :min_price AND :max_price AND l.brand = 'Hp' AND l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id
        """)
        # ทำการ execute SQL query ด้วย SQLAlchemy
        result = db.session.execute(query, {'min_price': min_price, 'max_price': max_price})
        
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list
    
    @staticmethod
    def filter_laptops_by_price_Apple(min_price, max_price):
        # สร้าง SQL query เพื่อดึงข้อมูลเครื่องโน้ตบุ๊กที่มีราคาอยู่ในช่วงที่ระบุ
        query = text("""
            SELECT l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img 
            FROM laptops l, graphic g, memory m, processor p, storage s2 
            WHERE prices BETWEEN :min_price AND :max_price AND l.brand = 'Apple' AND l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id
        """)
        # ทำการ execute SQL query ด้วย SQLAlchemy
        result = db.session.execute(query, {'min_price': min_price, 'max_price': max_price})
        
        Laptop_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])
            Laptop_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return Laptop_list   
    
    @staticmethod
    def sort_search(sort_option):
        if sort_option == 'lowsort':
            laptops = Laptop1.sort_asc()
        elif sort_option == 'expensivesort':
            laptops = Laptop1.sort_desc()
        elif sort_option == 'start':
            laptops = Laptop1.sort_no()
        return laptops

    @staticmethod
    def sort_acer(sort_option):
        if sort_option == 'lowsort':
            laptops = Laptop1.acer_sort_asc()
        elif sort_option == 'expensivesort':
            laptops = Laptop1.acer_sort_desc()
        elif sort_option == 'start':
            laptops = Laptop1.acer_sort_no()
        return laptops
    @staticmethod
    def sort_lenovo(sort_option):
        if sort_option == 'lowsort':
            laptops = Laptop1.lenovo_sort_asc()
        elif sort_option == 'expensivesort':
            laptops = Laptop1.lenovo_sort_desc()
        elif sort_option == 'start':
            laptops = Laptop1.lenovo_sort_no()
        return laptops   
    @staticmethod
    def sort_apple(sort_option):
        if sort_option == 'lowsort':
            laptops = Laptop1.apple_sort_asc()
        elif sort_option == 'expensivesort':
            laptops = Laptop1.apple_sort_desc()
        elif sort_option == 'start':
            laptops = Laptop1.apple_sort_no()
        return laptops  
    @staticmethod
    def sort_asus(sort_option):
        if sort_option == 'lowsort':
            laptops = Laptop1.asus_sort_asc()
        elif sort_option == 'expensivesort':
            laptops = Laptop1.asus_sort_desc()
        elif sort_option == 'start':
            laptops = Laptop1.asus_sort_no()
        return laptops 
    @staticmethod
    def sort_dell(sort_option):
        if sort_option == 'lowsort':
            laptops = Laptop1.dell_sort_asc()
        elif sort_option == 'expensivesort':
            laptops = Laptop1.dell_sort_desc()
        elif sort_option == 'start':
            laptops = Laptop1.dell_sort_no()
        return laptops 
    @staticmethod
    def sort_hp(sort_option):
        if sort_option == 'lowsort':
            laptops = Laptop1.hp_sort_asc()
        elif sort_option == 'expensivesort':
            laptops = Laptop1.hp_sort_desc()
        elif sort_option == 'start':
            laptops = Laptop1.hp_sort_no()
        return laptops 
    @staticmethod
    def sort_msi(sort_option):
        if sort_option == 'lowsort':
            laptops = Laptop1.msi_sort_asc()
        elif sort_option == 'expensivesort':
            laptops = Laptop1.msi_sort_desc()
        elif sort_option == 'start':
            laptops = Laptop1.msi_sort_no()
        return laptops
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort_laptops_search', methods=['POST'])
def sort_laptops_search():
    sort_option = request.form['sort']
    laptops = Laptops.sort_search(sort_option)
    return render_template('search_results.html', laptops=laptops)

@app.route('/sort_laptops_acer', methods=['POST'])
def sort_laptops_acer():
    sort_option = request.form['sort']
    laptops = Laptops.sort_acer(sort_option)
    return render_template('Acer_list.html', laptops=laptops)
@app.route('/sort_laptops_lenovo', methods=['POST'])
def sort_laptops_lenovo():
    sort_option = request.form['sort']
    laptops = Laptops.sort_lenovo(sort_option)
    return render_template('Lenovo_list.html', laptops=laptops)
@app.route('/sort_laptops_asus', methods=['POST'])
def sort_laptops_asus():
    sort_option = request.form['sort']
    laptops = Laptops.sort_asus(sort_option)
    return render_template('Asus_list.html', laptops=laptops)
@app.route('/sort_laptops_apple', methods=['POST'])
def sort_laptops_apple():
    sort_option = request.form['sort']
    laptops = Laptops.sort_apple(sort_option)
    return render_template('Apple_list.html', laptops=laptops)
@app.route('/sort_laptops_dell', methods=['POST'])
def sort_laptops_dell():
    sort_option = request.form['sort']
    laptops = Laptops.sort_dell(sort_option)
    return render_template('Dell_list.html', laptops=laptops)
@app.route('/sort_laptops_hp', methods=['POST'])
def sort_laptops_hp():
    sort_option = request.form['sort']
    laptops = Laptops.sort_hp(sort_option)
    return render_template('Hp_list.html', laptops=laptops)
@app.route('/sort_laptops_msi', methods=['POST'])
def sort_laptops_msi():
    sort_option = request.form['sort']
    laptops = Laptops.sort_msi(sort_option)
    return render_template('Msi_list.html', laptops=laptops)

@app.route('/Lenovo_list')
def lenovo_list():
    lenovo_laptops = Laptop1.lenovo_list()
    return render_template('Lenovo_list.html', laptops=lenovo_laptops)

@app.route('/Acer_list')
def acer_list():
    acer_laptops = Laptop1.acer_list()
    return render_template('Acer_list.html', laptops=acer_laptops)

@app.route('/Hp_list')
def hp_list():
    hp_laptops = Laptop1.hp_list()
    return render_template('Hp_list.html', laptops=hp_laptops)

@app.route('/Dell_list')
def dell_list():
    dell_laptops = Laptop1.dell_list()
    return render_template('dell_list.html', laptops=dell_laptops)

@app.route('/Msi_list')
def msi_list():
    msi_laptops = Laptop1.msi_list()
    return render_template('Msi_list.html', laptops=msi_laptops)

@app.route('/Asus_list')
def asus_list():
    asus_laptops = Laptop1.asus_list()
    return render_template('Asus_list.html', laptops=asus_laptops)

@app.route('/Apple_list')
def apple_list():
    apple_laptops = Laptop1.apple_list()
    return render_template('Apple_list.html', laptops=apple_laptops)

@app.route('/laptop/<int:laptop_id>')
def laptop_information(laptop_id):
    laptop_data = Laptop2.laptop_information(laptop_id)
    if laptop_data:
        return render_template('laptop_information.html', laptop=laptop_data)
    else:
        return "ไม่พบข้อมูลเครื่องคอมพิวเตอร์"

@app.route('/search', methods=['GET', 'POST'])
def search_laptop():
    if request.method == 'POST':
        search_query = request.form['search_query']  # รับคำค้นหาจากฟอร์ม
        laptops = Laptop3.search_result(search_query)  # เรียกใช้เมทอด search_result ใน model Laptop3
        if not laptops:  # ตรวจสอบว่าไม่มีข้อมูลที่ตรงกับคำค้นหา
            return render_template("search_notfound.html")
        else:
            return render_template('search_results.html', laptops=laptops)
    else:
        return render_template("search_notfound.html")
    
@app.route('/filter_laptops', methods=['POST'])
def filter_laptops():
    selected_brands = request.form.getlist('brand')
    filtered_laptops = Laptops.filter_laptop_by_brand(selected_brands)
    return render_template('filtered_laptops.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_ram', methods=['POST'])
def filter_laptops_by_ram():
    selected_ram = request.form.getlist('ram')
    filtered_laptops = Laptops.filter_laptop_by_ram(selected_ram)
    return render_template('filtered_laptops.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_ram_Lenovo', methods=['POST'])
def filter_laptops_by_ram_Lenovo():
    selected_ram = request.form.getlist('ram')
    filtered_laptops = Laptops.filter_laptop_by_ram_Lenovo(selected_ram)
    if not filtered_laptops:  # ถ้าไม่มีข้อมูลที่ถูกกรอง
        return render_template('search_notfound.html')
    else:
        return render_template('Lenovo_list.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_ram_Acer', methods=['POST'])
def filter_laptops_by_ram_Acer():
    selected_ram = request.form.getlist('ram')
    filtered_laptops = Laptops.filter_laptop_by_ram_Acer(selected_ram)
    if not filtered_laptops:  # ถ้าไม่มีข้อมูลที่ถูกกรอง
        return render_template('search_notfound.html')
    else:
        return render_template('Acer_list.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_ram_MSI', methods=['POST'])
def filter_laptops_by_ram_MSI():
    selected_ram = request.form.getlist('ram')
    filtered_laptops = Laptops.filter_laptop_by_ram_MSI(selected_ram)
    if not filtered_laptops:  # ถ้าไม่มีข้อมูลที่ถูกกรอง
        return render_template('search_notfound.html')
    else:
        return render_template('MSI_list.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_ram_Asus', methods=['POST'])
def filter_laptops_by_ram_Asus():
    selected_ram = request.form.getlist('ram')
    filtered_laptops = Laptops.filter_laptop_by_ram_Asus(selected_ram)
    if not filtered_laptops:  # ถ้าไม่มีข้อมูลที่ถูกกรอง
        return render_template('search_notfound.html')
    else:
        return render_template('Asus_list.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_ram_Dell', methods=['POST'])
def filter_laptops_by_ram_Dell():
    selected_ram = request.form.getlist('ram')
    filtered_laptops = Laptops.filter_laptop_by_ram_Dell(selected_ram)
    if not filtered_laptops:  # ถ้าไม่มีข้อมูลที่ถูกกรอง
        return render_template('search_notfound.html')
    else:
        return render_template('Dell_list.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_ram_Hp', methods=['POST'])
def filter_laptops_by_ram_Hp():
    selected_ram = request.form.getlist('ram')
    filtered_laptops = Laptops.filter_laptop_by_ram_Hp(selected_ram)
    if not filtered_laptops:  # ถ้าไม่มีข้อมูลที่ถูกกรอง
        return render_template('search_notfound.html')
    else:
        return render_template('Hp_list.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_ram_Apple', methods=['POST'])
def filter_laptops_by_ram_Apple():
    selected_ram = request.form.getlist('ram')
    filtered_laptops = Laptops.filter_laptop_by_ram_Apple(selected_ram)
    if not filtered_laptops:  # ถ้าไม่มีข้อมูลที่ถูกกรอง
        return render_template('search_notfound.html')
    else:
        return render_template('Apple_list.html', laptops=filtered_laptops)


@app.route('/filter_laptops_by_hdd', methods=['POST'])
def filter_laptops_by_hdd():
    selected_hdd = request.form.getlist('hdd_capacity')
    filtered_laptops = Laptops.filter_laptop_by_hdd(selected_hdd)
    return render_template('filtered_laptops.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_hdd_Lenovo', methods=['POST'])
def filter_laptops_by_hdd_Lenovo():
    selected_hdd = request.form.getlist('hdd_capacity')
    filtered_laptops = Laptops.filter_laptop_by_hdd_Lenovo(selected_hdd)
    if not filtered_laptops:  # ถ้าไม่มีข้อมูลที่ถูกกรอง
        return render_template('search_notfound.html')
    else:
        return render_template('Lenovo_list.html', laptops=filtered_laptops)


@app.route('/filter_laptops_by_hdd_Acer', methods=['POST'])
def filter_laptops_by_hdd_Acer():
    selected_hdd = request.form.getlist('hdd_capacity')
    filtered_laptops = Laptops.filter_laptop_by_hdd_Acer(selected_hdd)
    if not filtered_laptops:  # ถ้าไม่มีข้อมูลที่ถูกกรอง
        return render_template('search_notfound.html')
    else:
        return render_template('Acer_list.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_hdd_MSI', methods=['POST'])
def filter_laptops_by_hdd_MSI():
    selected_hdd = request.form.getlist('hdd_capacity')
    filtered_laptops = Laptops.filter_laptop_by_hdd_MSI(selected_hdd)
    if not filtered_laptops:  # ถ้าไม่มีข้อมูลที่ถูกกรอง
        return render_template('search_notfound.html')
    else:
        return render_template('MSI_list.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_hdd_Asus', methods=['POST'])
def filter_laptops_by_hdd_Asus():
    selected_hdd = request.form.getlist('hdd_capacity')
    filtered_laptops = Laptops.filter_laptop_by_hdd_Asus(selected_hdd)
    if not filtered_laptops:  # ถ้าไม่มีข้อมูลที่ถูกกรอง
        return render_template('search_notfound.html')
    else:
        return render_template('Asus_list.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_hdd_Dell', methods=['POST'])
def filter_laptops_by_hdd_Dell():
    selected_hdd = request.form.getlist('hdd_capacity')
    filtered_laptops = Laptops.filter_laptop_by_hdd_Dell(selected_hdd)
    if not filtered_laptops:  # ถ้าไม่มีข้อมูลที่ถูกกรอง
        return render_template('search_notfound.html')
    else:
        return render_template('Dell_list.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_hdd_Hp', methods=['POST'])
def filter_laptops_by_hdd_Hp():
    selected_hdd = request.form.getlist('hdd_capacity')
    filtered_laptops = Laptops.filter_laptop_by_hdd_Hp(selected_hdd)
    if not filtered_laptops:  # ถ้าไม่มีข้อมูลที่ถูกกรอง
        return render_template('search_notfound.html')
    else:
        return render_template('Hp_list.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_hdd_Apple', methods=['POST'])
def filter_laptops_by_hdd_Apple():
    selected_hdd = request.form.getlist('hdd_capacity')
    filtered_laptops = Laptops.filter_laptop_by_hdd_Apple(selected_hdd)
    if not filtered_laptops:  # ถ้าไม่มีข้อมูลที่ถูกกรอง
        return render_template('search_notfound.html')
    else:
        return render_template('Apple_list.html', laptops=filtered_laptops)


@app.route('/filter_laptops_by_price', methods=['POST'])
def filter_laptops_by_price():
    min_price = request.form['min_price']
    max_price = request.form['max_price']
    
    filtered_laptops = Laptops.filter_laptops_by_price(min_price, max_price)
    
    if not filtered_laptops:
        return render_template('search_notfound.html')
    else:
        return render_template('filtered_laptops.html', laptops=filtered_laptops)
    
@app.route('/filter_laptops_by_price_Lenovo', methods=['POST'])
def filter_laptops_by_price_Lenovo():
    min_price = request.form['min_price']
    max_price = request.form['max_price']
    
    filtered_laptops = Laptops.filter_laptops_by_price_Lenovo(min_price, max_price)
    
    if not filtered_laptops:
        return render_template('search_notfound.html')
    else:
        return render_template('Lenovo_list.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_price_MSI', methods=['POST'])
def filter_laptops_by_price_MSI():
    min_price = request.form['min_price']
    max_price = request.form['max_price']
    
    filtered_laptops = Laptops.filter_laptops_by_price_MSI(min_price, max_price)
    
    if not filtered_laptops:
        return render_template('search_notfound.html')
    else:
        return render_template('MSI_list.html', laptops=filtered_laptops)
    
@app.route('/filter_laptops_by_price_Acer', methods=['POST'])
def filter_laptops_by_price_Acer():
    min_price = request.form['min_price']
    max_price = request.form['max_price']
    
    filtered_laptops = Laptops.filter_laptops_by_price_Acer(min_price, max_price)
    
    if not filtered_laptops:
        return render_template('search_notfound.html')
    else:
        return render_template('Acer_list.html', laptops=filtered_laptops)
    
@app.route('/filter_laptops_by_price_Asus', methods=['POST'])
def filter_laptops_by_price_Asus():
    min_price = request.form['min_price']
    max_price = request.form['max_price']
    
    filtered_laptops = Laptops.filter_laptops_by_price_Asus(min_price, max_price)
    
    if not filtered_laptops:
        return render_template('search_notfound.html')
    else:
        return render_template('Asus_list.html', laptops=filtered_laptops)
    
@app.route('/filter_laptops_by_price_Dell', methods=['POST'])
def filter_laptops_by_price_Dell():
    min_price = request.form['min_price']
    max_price = request.form['max_price']
    
    filtered_laptops = Laptops.filter_laptops_by_price_Dell(min_price, max_price)
    
    if not filtered_laptops:
        return render_template('search_notfound.html')
    else:
        return render_template('Dell_list.html', laptops=filtered_laptops)

@app.route('/filter_laptops_by_price_Hp', methods=['POST'])
def filter_laptops_by_price_Hp():
    min_price = request.form['min_price']
    max_price = request.form['max_price']
    
    filtered_laptops = Laptops.filter_laptops_by_price_Hp(min_price, max_price)
    
    if not filtered_laptops:
        return render_template('search_notfound.html')
    else:
        return render_template('Hp_list.html', laptops=filtered_laptops)
    
@app.route('/filter_laptops_by_price_Apple', methods=['POST'])
def filter_laptops_by_price_Apple():
    min_price = request.form['min_price']
    max_price = request.form['max_price']
    
    filtered_laptops = Laptops.filter_laptops_by_price_Apple(min_price, max_price)
    
    if not filtered_laptops:
        return render_template('search_notfound.html')
    else:
        return render_template('Apple_list.html', laptops=filtered_laptops)

@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')

@app.route('/notfound')
def notfound():
    return render_template('notfound.html')

@app.route('/recommendation_spec1')
def recommendation_spec1():
    return render_template('recom/1_spec.html')

@app.route('/recommendation_spec_medium_os1')
def recommendation_spec_medium_os1():
    return render_template('recom/1_spec_medium_os.html')

@app.route('/recommendation_spec_medium_os_touch1')
def recommendation_spec_medium_os_touch1():
    return render_template('recom/1_spec_medium_os_touch.html')

@app.route('/recommendation_spec2')
def recommendation_spec2():
    return render_template('recom/2_spec.html')

@app.route('/recommendation_spec_low_os2')
def recommendation_spec_low_os2():
    return render_template('recom/2_spec_low_os.html')

@app.route('/recommendation_spec3')
def recommendation_spec3():
    return render_template('recom/3_spec.html')

@app.route('/recommendation_spec_medium_os3')
def recommendation_spec_medium_os3():
    return render_template('recom/3_spec_medium_os.html')

@app.route('/recommendation_spec4')
def recommendation_spec4():
    return render_template('recom/4_spec.html')

@app.route('/recommendation_spec_medium_os4')
def recommendation_spec_medium_os4():
    return render_template('recom/4_spec_medium_os.html')

@app.route('/recommendation_spec5')
def recommendation_spec5():
    return render_template('recom/5_spec.html')

@app.route('/compare_laptop', methods=['POST'])
def compare_laptop():
    # รับรายการของไอดีที่ต้องการเปรียบเทียบจาก form
    compare_laptop_ids = request.form.getlist('compare_laptop_ids')
    
    # เรียกใช้งานฟังก์ชัน compare_laptop ในคลาส Laptop2 เพื่อดึงข้อมูลของแล็ปท็อปสองเครื่อง
    laptops = Laptop2.compare_laptop(compare_laptop_ids[0], compare_laptop_ids[1])

    # เรียกใช้งานเทมเพลต compare_laptop.html และส่งข้อมูลของแล็ปท็อปที่เปรียบเทียบไปที่เทมเพลต
    return render_template('compare_laptop.html', laptops=laptops)


@app.route('/recommendation_list')
def recommendation_list():
    rule = request.args.get('rule')
    laptops = None
    rule_functions = {
        'rule1': Laptop1.rule1,
        'rule2': Laptop1.rule2,
        'rule3': Laptop1.rule3,
        'rule4': Laptop1.rule4,
        'rule5': Laptop1.rule5,
        'rule6': Laptop1.rule6,
        'rule7': Laptop1.rule7,
        'rule8': Laptop1.rule8,
        'rule9': Laptop1.rule9,
        'rule10': Laptop1.rule10,
        'rule11': Laptop1.rule11,
        'rule12': Laptop1.rule12,
        'rule13': Laptop1.rule13,
        'rule14': Laptop1.rule14,
        'rule15': Laptop1.rule15,
        'rule16': Laptop1.rule16,
        'rule17': Laptop1.rule17,
        'rule18': Laptop1.rule18,
    }

    laptops = rule_functions.get(rule, lambda: None)()
    return render_template('recommendation_list.html',laptops=laptops)


if __name__ == '__main__':
    app.run(debug=True)

