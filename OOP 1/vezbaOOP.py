from product import Product
from Schoppingcart import Shoppingcart

Iphone16 = Product("iphone16 pro",1500,15,"ios")
samsungS25 = Product("samsung ", 2500, 110, "android")
nokia = Product("Nokia", 500, 50, "android")


phonecart = Shoppingcart()
phonecart.add_product(Iphone16)
phonecart.add_product(Iphone16)
phonecart.add_product(Iphone16)
phonecart.add_product(samsungS25)
phonecart.add_product(samsungS25)
phonecart.add_product(samsungS25)


phonecart.show_products()
print(Product.number_of_types)

