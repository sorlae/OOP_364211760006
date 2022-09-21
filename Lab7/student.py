"""
Name: Chinanat Sorlae
ID: 364211760006
Group: MIT221
"""

class Student:
    def __init__(self,name,id):
        # attributes
        self.name = name # public member
        self.__id = id # private member
    def __str__(self):
        print(f'Name: {self.name} ID: {self.__id}')

std = Student("Chinanat","006")
# direct access
#print(std.name, std.id)

std.__str__()

std.name = "Maneenuch" # change data attribute
std.__str__()

std.__id = "060"
std.__str__()

# name mangling
print(std._Student__id)

std._Student__id = "060"
std.__str__()


