# Import libraries
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask import Flask
from app import app, db



    
# ทำโมเดล+เขียนคำสั่ง SQL
class Laptop1:
    def __init__(self, laptop_id,model, cpu_model,graphic_chip,ram,hdd_capacity,prices,img):
        self.model = model
        self.cpu_model = cpu_model
        self.laptop_id = laptop_id
        self.graphic_chip = graphic_chip
        self.ram = ram
        self.hdd_capacity = hdd_capacity
        self.prices = prices
        self.img= img  
            
    @staticmethod
    def connector():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ppgdmild",
            database="laptopdb"
        )
        return connection

    # รายการ Lenovo
    @staticmethod
    def lenovo_list():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.brand = 'Lenovo' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        lenovo_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            lenovo_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return lenovo_list #ลิสต์ข้อมูล
    
    # รายการ Lenovo
    @staticmethod
    def acer_list():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.brand = 'Acer' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_list #ลิสต์ข้อมูล
    
        # รายการ Lenovo
    @staticmethod
    def apple_list():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.brand = 'Apple' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        apple_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            apple_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return apple_list #ลิสต์ข้อมูล
    
        # รายการ Lenovo
    @staticmethod
    def asus_list():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.brand = 'Asus' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        asus_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            asus_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return asus_list #ลิสต์ข้อมูล
    
    @staticmethod
    def dell_list():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.brand = 'Dell' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        dell_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            dell_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return dell_list #ลิสต์ข้อมูล
    
        # รายการ Lenovo
    @staticmethod
    def hp_list():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.brand = 'Hp' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        hp_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            hp_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return hp_list #ลิสต์ข้อมูล
    
    @staticmethod
    def msi_list():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.brand = 'Msi' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        msi_list = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            msi_list.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return msi_list #ลิสต์ข้อมูล
    

    
    @staticmethod
    def rule1():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 1' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule1 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule1.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule1 #ลิสต์ข้อมูล
    
    @staticmethod
    def rule2():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 2' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule2 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule2.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule2 #ลิสต์ข้อมูล
    
    @staticmethod
    def rule3():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 3' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule3 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule3.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule3 #ลิสต์ข้อมูล
    
    @staticmethod
    def rule4():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 4' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule4 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule4.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule4 #ลิสต์ข้อมูล
    
    @staticmethod
    def rule5():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 5' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule5 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule5.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule5 #ลิสต์ข้อมูล
    @staticmethod
    def rule6():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 6' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule6 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule6.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule6 #ลิสต์ข้อมูล
    @staticmethod
    def rule7():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 7' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule7 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule7.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule7 #ลิสต์ข้อมูล
    @staticmethod
    def rule8():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 8' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule8 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule8.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule8 #ลิสต์ข้อมูล
    @staticmethod
    def rule9():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 9' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule9 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule9.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule9 #ลิสต์ข้อมูล
    @staticmethod
    def rule10():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 10' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule10 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule10.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule10 #ลิสต์ข้อมูล
    @staticmethod
    def rule11():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 11' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule11 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule11.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule11 #ลิสต์ข้อมูล
    @staticmethod
    def rule12():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 12' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule12 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule12.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule12 #ลิสต์ข้อมูล
    @staticmethod
    def rule13():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 13' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule13 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule13.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule13 #ลิสต์ข้อมูล
    @staticmethod
    def rule14():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 14' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule14 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule14.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule14 #ลิสต์ข้อมูล
    @staticmethod
    def rule15():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 15' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule15 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule15.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule15 #ลิสต์ข้อมูล
    @staticmethod
    def rule16():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 16' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule16 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule16.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule16 #ลิสต์ข้อมูล
    @staticmethod
    def rule17():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 17' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule17 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule17.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule17 #ลิสต์ข้อมูล
    @staticmethod
    def rule18():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = "select l.laptop_id,l.model,p.cpu_model,g.graphic_chip,m.ram,s2.hdd_capacity,l.prices,l.img from laptops l, graphic g, memory m, processor p, storage s2 where l.rule = 'Rule: 18' and l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id" 
        cursor.execute(query)
        result = cursor.fetchall()
        rule18 = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            rule18.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return rule18 #ลิสต์ข้อมูล

    @staticmethod
    def sort_asc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        ORDER BY l.prices ASC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        sort_asc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            sort_asc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return sort_asc #ลิสต์ข้อมูล
    @staticmethod
    def sort_desc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        ORDER BY l.prices DESC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        sort_desc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            sort_desc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return sort_desc #ลิสต์ข้อมูล
    @staticmethod
    def sort_no():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        sort_no = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            sort_no.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return sort_no #ลิสต์ข้อมูล
    
    @staticmethod
    def acer_sort_asc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Acer'
        ORDER BY l.prices ASC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_asc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_asc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_asc #ลิสต์ข้อมูล
    @staticmethod
    def acer_sort_desc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Acer'
        ORDER BY l.prices DESC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_desc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_desc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_desc #ลิสต์ข้อมูล
    @staticmethod
    def acer_sort_no():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Acer'
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_no = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_no.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_no #ลิสต์ข้อมูล
    @staticmethod
    def lenovo_sort_asc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Lenovo'
        ORDER BY l.prices ASC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        lenovo_sort_asc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            lenovo_sort_asc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return lenovo_sort_asc #ลิสต์ข้อมูล
    
    @staticmethod
    def lenovo_sort_desc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Lenovo'
        ORDER BY l.prices DESC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        lenovo_sort_desc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            lenovo_sort_desc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return lenovo_sort_desc #ลิสต์ข้อมูล
    @staticmethod
    def lenovo_sort_no():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Lenovo'
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        lenovo_sort_no = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            lenovo_sort_no.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return lenovo_sort_no #ลิสต์ข้อมูล
    
    @staticmethod
    def apple_sort_asc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Apple'
        ORDER BY l.prices ASC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        apple_sort_asc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            apple_sort_asc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return apple_sort_asc #ลิสต์ข้อมูล
    @staticmethod
    def apple_sort_desc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Apple'
        ORDER BY l.prices DESC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_desc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_desc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_desc #ลิสต์ข้อมูล
    @staticmethod
    def apple_sort_no():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Apple'
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_no = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_no.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_no #ลิสต์ข้อมูล
    
    @staticmethod
    def asus_sort_asc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Asus'
        ORDER BY l.prices ASC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_asc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_asc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_asc #ลิสต์ข้อมูล
    @staticmethod
    def asus_sort_desc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Asus'
        ORDER BY l.prices DESC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_desc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_desc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_desc #ลิสต์ข้อมูล
    @staticmethod
    def asus_sort_no():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Asus'
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_no = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_no.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_no #ลิสต์ข้อมูล
    
    @staticmethod
    def dell_sort_asc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Dell'
        ORDER BY l.prices ASC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_asc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_asc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_asc #ลิสต์ข้อมูล
    @staticmethod
    def dell_sort_desc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Dell'
        ORDER BY l.prices DESC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_desc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_desc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_desc #ลิสต์ข้อมูล
    @staticmethod
    def dell_sort_no():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Dell'
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_no = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_no.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_no #ลิสต์ข้อมูล
    
    @staticmethod
    def hp_sort_asc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Hp'
        ORDER BY l.prices ASC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_asc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_asc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_asc #ลิสต์ข้อมูล
    @staticmethod
    def hp_sort_desc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Hp'
        ORDER BY l.prices DESC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_desc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_desc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_desc #ลิสต์ข้อมูล
    @staticmethod
    def Hp_sort_no():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Hp'
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_no = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_no.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_no #ลิสต์ข้อมูล
    
    @staticmethod
    def msi_sort_asc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Msi'
        ORDER BY l.prices ASC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_asc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_asc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_asc #ลิสต์ข้อมูล
    @staticmethod
    def msi_sort_desc():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Msi'
        ORDER BY l.prices DESC
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_desc = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_desc.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_desc #ลิสต์ข้อมูล
    @staticmethod
    def msi_sort_no():
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop1.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
        FROM laptops l
        JOIN graphic g ON l.gpu_id = g.gpu_id
        JOIN memory m ON l.memory_id = m.memory_id
        JOIN processor p ON l.processor_id = p.processor_id
        JOIN storage s2 ON l.storage_id = s2.storage_id
        WHERE l.brand = 'Msi'
        """ 
        cursor.execute(query)
        result = cursor.fetchall()
        acer_sort_no = []
        for row in result: 
            prices_with_comma = '{:,}'.format(row[6])  # แปลง prices เป็นรูปแบบที่มีเครื่องหมาย ","
            acer_sort_no.append(Laptop1(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        return acer_sort_no #ลิสต์ข้อมูล




class Laptop2:
    def __init__(self, laptop_id,brand,model,img,wifi,bluetooth,web_camera,description,pros,cons,io_ports,
                 cpu_brand,cpu_model,base_clock,boost_clock,cache,
                 graphic_brand,graphic_chip,ram,ram_type,hdd_capacity,hdd_type,
                 prices,battery,os,store_name,url_buy,display_size,display_specs,display_type,touchscreen):
        self.brand = brand
        self.model = model
        self.img= img 
        self.pros = pros
        self.cons = cons
        self.io_ports = io_ports
        
        self.wifi = wifi
        self.bluetooth = bluetooth
        self.web_camera = web_camera
        
        self.graphic_brand = graphic_brand 
        self.graphic_chip = graphic_chip
        
        self.cpu_model = cpu_model
        self.cpu_brand = cpu_brand
        self.base_clock = base_clock
        self.boost_clock = boost_clock
        self.cache = cache
        
        self.ram = ram
        self.ram_type = ram_type
        
        self.hdd_capacity = hdd_capacity
        self.hdd_type = hdd_type
        
        self.prices = prices
      
        self.display_size = display_size
        self.display_specs = display_specs
        self.display_type = display_type
        self.touchscreen = touchscreen
        
        self.os = os
        self.description = description
        self.battery = battery
        self.laptop_id = laptop_id

        self.store_name = store_name
        self.url_buy = url_buy
    
            
    @staticmethod
    def connector():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ppgdmild",
            database="laptopdb"
        )
        return connection
    
    @staticmethod
    def laptop_information(laptop_id):
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop2.connector()
        cursor = connection.cursor()
        query = "select l.brand,l.model, l.img,c.wifi,c.bluetooth,l.web_camera,l.description,l.pros,l.cons,l.io_ports,p.cpu_brand,p.cpu_model,p.base_clock,p.boost_clock,p.cache,g.graphic_brand,g.graphic_chip,m.ram,m.ram_type,s2.hdd_capacity,s2.hdd_type,l.prices,l.battery,l.os,s.store_name,s.url_buy,d.display_size,d.display_specs,d.display_type,d.touchscreen from laptops l, connection as c, display d, graphic g, laptop_store s, memory m, processor p, storage s2 where l.gpu_id=g.gpu_id and l.memory_id=m.memory_id and l.display_id=d.display_id and l.storage_id = s2.storage_id and l.processor_id=p.processor_id and l.connection_id = c.connection_id and l.store_id=s.store_id and l.laptop_id = %s"
        cursor.execute(query, (laptop_id,))
        result = cursor.fetchone()  # ใช้ fetchone() เนื่องจากต้องการเฉพาะแถวเดียว
        if result:
            # ส่งอาร์กิวเมนต์ให้กับเมทอด __init__ ของคลาส Laptop ในการสร้างอ็อบเจกต์
            prices_with_comma = '{:,}'.format(result[21])  # 21 เป็น index ของราคาใน result
            laptop = Laptop2(laptop_id, *result[:21], prices_with_comma, *result[22:])
            return laptop
        else:
            return None  # หากไม่พบข้อมูล
    
    @property
    def formatted_pros(self):
        return self.pros.split('.')
    
    @property
    def formatted_cons(self):
        return self.cons.split('.')
    
    @property
    def formatted_io(self):
        return self.io_ports.split(',')
    
    @staticmethod
    def compare_laptop(laptop_id_1, laptop_id_2):
        # เชื่อมต่อฐานข้อมูล
        connection = Laptop2.connector()
        cursor = connection.cursor()
        query = """
        SELECT l.brand, l.model, l.img, c.wifi, c.bluetooth, l.web_camera, l.description, l.pros, l.cons, l.io_ports, 
        p.cpu_brand, p.cpu_model, p.base_clock, p.boost_clock, p.cache, 
        g.graphic_brand, g.graphic_chip, m.ram, m.ram_type, s2.hdd_capacity, s2.hdd_type, 
        l.prices, l.battery, l.os, s.store_name, s.url_buy, d.display_size, d.display_specs, d.display_type, 
        d.touchscreen 
        FROM laptops l 
        JOIN connection c ON l.connection_id = c.connection_id 
        JOIN display d ON l.display_id = d.display_id 
        JOIN graphic g ON l.gpu_id = g.gpu_id 
        JOIN laptop_store s ON l.store_id = s.store_id 
        JOIN memory m ON l.memory_id = m.memory_id 
        JOIN processor p ON l.processor_id = p.processor_id 
        JOIN storage s2 ON l.storage_id = s2.storage_id 
        WHERE l.laptop_id IN (%s, %s)
        """
        cursor.execute(query, (laptop_id_1, laptop_id_2))
        results = cursor.fetchall()
        laptops = []
        for result in results:
            prices_with_comma = '{:,}'.format(result[21])
            laptop = Laptop2(result[0], *result[:21], prices_with_comma, *result[22:])
            laptops.append(laptop)
        return laptops
    
app = Flask(__name__, template_folder='pages', static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ppgdmild@localhost/laptopdb'
db = SQLAlchemy()
db.init_app(app)

class Laptop3(db.Model):
    def __init__(self,laptop_id,model, cpu_model,graphic_chip,ram,hdd_capacity,prices,img):
        self.model = model
        self.cpu_model = cpu_model
        self.laptop_id = laptop_id
        self.graphic_chip = graphic_chip
        self.ram = ram
        self.hdd_capacity = hdd_capacity
        self.prices = prices
        self.img= img 
        
    #__tablename__ = 'laptops'

    laptop_id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100))
    print(model)
    
    def connector():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ppgdmild",
            database="laptopdb"
        )
        return connection
    
    @staticmethod
    def search_result(search):
    
        connection = Laptop3.connector()
        cursor = connection.cursor()
        
        # เขียนคำสั่ง SQL query สำหรับค้นหาข้อมูล
        query = """
            SELECT l.laptop_id, l.model, p.cpu_model, g.graphic_chip, m.ram, s2.hdd_capacity, l.prices, l.img 
            FROM laptops l, graphic g, memory m, processor p, storage s2 
            WHERE l.model LIKE %s AND l.gpu_id=g.gpu_id AND l.memory_id=m.memory_id AND l.storage_id = s2.storage_id AND l.processor_id=p.processor_id
        """
        
        # ทำการ execute query โดยใส่ค่าคำค้นหาลงไปในตำแหน่งที่ต้องการ
        cursor.execute(query, (f'%{search}%',))
        
        # ดึงผลลัพธ์ทั้งหมดจาก cursor
        result = cursor.fetchall()
        
        # สร้างลิสต์เพื่อเก็บข้อมูลที่ค้นหาได้
        search_results = []
        for row in result: 
            # แปลงราคาเป็นรูปแบบที่มีเครื่องหมายคอมมา ","
            prices_with_comma = '{:,}'.format(row[6])
            # เพิ่มข้อมูลเข้าไปในลิสต์ search_results
            search_results.append(Laptop3(row[0], row[1], row[2], row[3], row[4], row[5], prices_with_comma, row[7]))
        
        # คืนค่าลิสต์ข้อมูลที่ค้นหาได้
        return search_results    




    
    
        
        
