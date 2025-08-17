
#Prikazi najskuplji proizvod


products = {
    "hleb": {
        "cena": 100,
        "kolicina": 50

    },
    "pivo": {
        "cena": 150,
        "kolicina": 220
    }

}
# Izlistaj -> print
option = None
allowed_option = [
    "dodaj", "obrishi", "izlistaj",
    "stop", "istorijat", "obrishi sve"
    "prikazi najskuplji proizvod", "pnp"
]
history = []

while option not in allowed_option:
    option = input(f"Sta zelite da odradite : {", ".join(allowed_option)}  \n").lower()

    if option == "obrishi":
        product = None

        while product not in products:
            product = input("Unesite ime proizvoda za brishenje : \n").lower()

        del products[product]
        option = None
        msg = f"Obrisaliste proizvod {product} \n"
        print(msg)
        history.append(msg)

    elif option == "dodaj":
        product = None

        while product in products or product is None:
            product = input("Unesite ime proizvoda koje ne postoji:  \n")

        product_price = None

        while product_price is None or product_price <= 0:
            product_price = int(input("unesite cena proizvoda \n "))

        product_amaunt = None
        while product_amaunt is None or product_amaunt <= 0:
            product_amaunt = int(input("Unesite Kolicina prozivoda : \n"))

        products[product] = {
            "cena": product_price,
            "kolicina": product_amaunt

        }

        option = None

        msg = f"Dodali ste novi proizvod {product}   \n"
        print(msg)
        history.append(msg)

    elif option == "izlistaj":
        print(products)
        product = None

    elif option == "istorijat":
        print(history)
        option = None

    elif option == "obrishi sve" :
        products = {}
        option = None
    elif option == "prikazi najskuplji proizvod" or "pnp" :
        highest_price = 0
        most_expensive_product = None

        for product in products :
            if highest_price < products[product]["cena"] :
                highest_price = products[product]["cena"]
                most_expensive_product = product
        print(products[most_expensive_product]["cena"])



print(products)