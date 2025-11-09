# Product
# name, price, amaunt, type
#food , technology...
from tkinter.font import names


class Product :

    def __init__(self , name, price, amaunt, type):
        self.name = name
        self.price = price
        self.amaunt = amaunt
        self.type = type


iPhone = Product("Iphone 15", 1400, 100, "ProMax")

print(iPhone.name, iPhone.amaunt, iPhone.price)

samsung = Product("samsung 24", 500, 120, "Ultralook")
print(samsung.name)