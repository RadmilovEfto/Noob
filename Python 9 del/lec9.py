# virtualna biblioteka
#Crud
# Dodaj Knigu
#izlistaj knigu
# Obrishi Knigu

books = [
    {
        "name" : "Harry Poter 1 "

}]

books.append({"Harry Poter 1"})
print(books)
def calculate_delivery(city):
    if city == "Beograd" or city == "Zagreb" :
        return 500
    elif city == "Subotica" :
        return 1200
    elif city == "Novi Sad" :
        return 700
    elif city == "Split" :
        return 800
    else :
       return -1
product_price = 200
belgrade_delivery = calculate_delivery("Beograd")
subotica_delivery = calculate_delivery("Subotica")
total_price = product_price + belgrade_delivery
print(f"vasa narachka koshta {product_price},  a vasha dostava iznosi {belgrade_delivery}, se ukopno iznosi : {total_price}")


