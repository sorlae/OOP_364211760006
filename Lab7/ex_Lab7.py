"""
Name: Chinanat Sorlae
ID: 364211760006
Group: MIT221
"""

class Labtop:
    def __init__(self, brand, model, cpu, ram, display, storage, price):
        # attributes
        # private member
        self.__brand = brand
        self.__model = model
        self.__cpu = cpu
        self.__ram = ram
        self.__display = display
        self.__storage = storage
        self.__price = price

    # getter and setter Brand
    def get_brand(self):
        return self.__brand
    def set_brand(self,brand):
        self.__brand = brand

    # getter and setter Model
    def get_model(self):
        return self.__model
    def set_model(self,model):
        self.__model = model

    # getter and setter CPU
    def get_cpu(self):
        return self.__cpu
    def set_CPU(self,cpu):
        self.__cpu = cpu

    # getter and setter RAM
    def get_ram(self):
        return self.__ram
    def set_ram(self,ram):
        self.__ram = ram

    # getter and setter Display
    def get_display(self):
        return self.__display
    def set_display(self,display):
        self.__display = display

    # getter and setter Storage
    def get_storage(self):
        return self.__storage
    def set_storage(self,storage):
        self.__storage = storage

    # getter and setter Price
    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price = price

    def __str__(self):
        print(f'Brand: {self.__brand} '
              f'Model: {self.__model} '
              f'CPU: {self.__cpu}'
              f'RAM: {self.__ram}'
              f'Display: {self.__display}'
              f'Storage: {self.__storage}'
              f'Price: {self.__price}')

print("--------------------------------------")
L = Labtop("ASUS","Vivobook 15X","Intel Core i5-12500H","8","15.6","512","27990")
L.__str__()

print("--------------------------------------")

L.set_brand("Lenovo")
print(L.get_brand())

L.set_model("idelPad Garning 3")
print(L.get_model())

L.set_CPU("Intel Core i5-11320H")
print(L.get_cpu())

L.set_ram("9")
print(L.get_ram())

L.set_display("16.5")
print(L.get_display())

L.set_storage("513")
print(L.get_storage())

L.set_price("25990")
print(L.get_price())

print("--------------------------------------")

L.__str__()

print("--------------------------------------")