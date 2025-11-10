
class Product :
    number_of_product = 0

    def __init__(self , name, price, amaunt, type):
        if amaunt < 1 :
            raise ValueError("Amaunt must be more then 0")

        self.name = name
        self.price = price
        self.amaunt = amaunt
        self.type = type
        Product.number_of_product += 1

