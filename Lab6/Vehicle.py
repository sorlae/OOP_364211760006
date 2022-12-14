"""
Name: Chinanat Sorlae
ID: 364211760006
Group: MIT221
"""

"""
OOP Exercise Chapter 6

1. จงเขียนโปรแกรมภาษาไพธอนเพื่อสร้างคลาสพาหนะชื่อ Vehicle ที่ประกอบไปด้วยคุณลักษณะ (attributes) คือ 
ยี่ห้อรถ (brand) 
รุ่นรถ (model)
สีรถ (color)
ความเร็วสูงสุด (max speed)
ราคา (price)

2.จากข้อที่ 1 เขียนโปรแกรมเพื่อสร้างวัตถุ (object) จากคลาส Vehicle โดยรับข้อมูลจากผู้ใช้ตามคุณลักษณะ (attributes)ของคลาส
จากนั้นแสดงข้อมูลทางหน้าจอภาพ

15 นาที;/;
"""

class Vehicle:
    #class attribute
    my_vehicle = []

    def __init__(self,brand,model,color,max_speed,price):
        self.brand = brand
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.price = price
        self.my_vehicle.append(self)

    def vehicle_detail(self):
        print(f'Brand:{self.brand} '
              f'Model:{self.model} '
              f'Color:{self.color} '
              f'Max_speed:{self.max_speed} '
              f'Price:{self.price}')