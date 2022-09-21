"""
Name: Chinanat Sorlae
ID: 364211760006
Group: MIT221
"""

class Labtop:
    def __init__(self,Brand,Model,CPU,RAM,Display,Storage,Price):
        # attributes
        # private member
        self.__Brand = Brand
        self.__Model = Model
        self.__CPU = CPU
        self.__RAM = RAM
        self.__Display = Display
        self.__Storage = Storage
        self.__Price = Price

    # getter and setter Brand
    def get_Brand(self):
        return self.__Brand
    def set_Brand(self,Brand):
        self.__Brand = Brand

    # getter and setter Model
    def get_Model(self):
        return self.__Model
    def set_Model(self,Model):
        self.__Model = Model

    # getter and setter CPU
    def get_CPU(self):
        return self.__CPU
    def set_CPU(self,CPU):
        self.__CPU = CPU

    # getter and setter RAM
    def get_RAM(self):
        return self.__RAM
    def set_RAM(self,RAM):
        self.__RAM = RAM

    # getter and setter Display
    def get_Display(self):
        return self.__Display
    def set_Display(self,Display):
        self.__Display = Display

    # getter and setter Storage
    def get_Storage(self):
        return self.__Storage
    def set_Storage(self,Storage):
        self.__Storage = Storage

    # getter and setter Price
    def get_Price(self):
        return self.__Price
    def set_Price(self,Price):
        self.__Price = Price

    def __str__(self):
        print(f'Brand: {self.__Brand} '
              f'Model: {self.__Model} '
              f'CPU: {self.__CPU}'
              f'RAM: {self.__RAM}'
              f'Display: {self.__Display}'
              f'Storage: {self.__Storage}'
              f'Price: {self.__Price}')

print("--------------------------------------")
L = Labtop("ASUS","Vivobook 15X","Intel Core i5-12500H","8","15.6","512","27990")
L.__str__()

print("--------------------------------------")

L.set_Brand("Lenovo")
print(L.get_Brand())

L.set_Model("idelPad Garning 3")
print(L.get_Model())

L.set_CPU("Intel Core i5-11320H")
print(L.get_CPU())

L.set_RAM("9")
print(L.get_RAM())

L.set_Display("16.5")
print(L.get_Display())

L.set_Storage("513")
print(L.get_Storage())

L.set_Price("25990")
print(L.get_Price())

print("--------------------------------------")

L.__str__()

print("--------------------------------------")