

from DB import Db


class Product (Db):
    number_of_product = 0
    allowed_types = ['android', 'ios']
    number_of_types = {
        'android' : 0,
        'ios' : 0
    }


    def __init__(self  ):

        super().__init__()

    def create (self,name, price, amaunt, type ):

        if amaunt < 1 :
            raise ValueError("Amaunt must be more then 0")
        if type not in Product.allowed_types :
            raise ValueError("You don't pass the correct type")

        self.name = name
        self.price = price
        self.amaunt = amaunt
        self.type = type
        Product.number_of_product += 1

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO products (name, price, amaunt, type) VALUES (%s,%s,%s,%s)",
                       (name, price,amaunt, type))

        self.connection.commit()
        cursor.close()

        Product.number_of_types[type] += amaunt
