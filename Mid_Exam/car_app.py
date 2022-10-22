"""
Name: Chinanat Sorlae
ID: 364211760006
Group: MIT221
"""
from car import EV_Car

#display
def display_evcar():
    if len(display_ev_car) ==0:
        print("You had no car data.")
    else:
        print(f'You had {len(display_ev_car)} following:')
        for x in display_ev_car:
            x.display_evcar()
    print("\n")

# option
def display_option_system():
    select = 0
    print("Welcome to Car Data Store System (VDSS)")
    print("1. Add Car")
    print("2. Display all Car")
    print("3. exit")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_evcar_data()
    elif select == 2:
        display_evcar()
    elif select == 3:
        print("Thank You Love You Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-3.")



# input data
def input_evcar_data():
    No = int(input("Enter Car No: "))
    Brand = input("Enter Car Brand: ")
    Model = input("Enter Car Model: ")
    Motor = int(input("Enter Car Motor: "))
    Horse_Power = int(input("Enter Car Horse Power: "))
    Battery_Size = float(input("Enter Car Battery Size(kWh): "))
    Range = int(input("Enter Car Range(km): "))
    Price = int(input("Enter Car Price: "))

    display_ev_car.append(EV_Car(No,Brand,Model,Motor,Horse_Power,Battery_Size,Range,Price))
    print("\n-----------------------------------")
    print("Already add car to store.")
    print("-----------------------------------")

display_ev_car = []
s = 0
while s == 0:
    display_option_system()
