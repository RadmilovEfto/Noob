from product import Product
from Schoppingcart import Shoppingcart

Iphone16 = Product("iphone16 pro",1500,15,"proMax")
samasungS25 = Product("samsung ", 2500, 110, "S25")
nokia = Product("Nokia", 500, 50, "3310")


phonecart = Shoppingcart()
phonecart.add_product(Iphone16)

phonecart.show_products()


