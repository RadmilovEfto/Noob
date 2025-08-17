# Vezba 2
# Pitajte korisnika sta zeli da uradi :
# A : Obrise proizvode (obrisati) -> izvrsiti logiku za brisanje
# B : Dodaj proizvod (dodaj) -> "test"

# Pitaj korisnika sta zeli da uradi :
# A : Obrisi -> Unesite ime proizvoda za brisanje -> brisemo proizvod
# B : Dodaj -> Unesite proizvoda i cenu -> "test"
# skracheno za promena na productAmaunt je ctr + H
#camelCase stil -> nova rec pocinje sa velikom slovo stil pisanja e to
        #  U Python se korisiti snake_case u nashoj slucaj se koristi snake_case
# kako da mi kada korisnik obrishe ili doda proizvod opet da ga pitamo sta zeli da uradi? vracamo korisnika na pocetak
# Dodaj nova opcija u codu izlistaj, to moze da se uradi sa print.
# Dodaj opcija Stop !
# dodaj istorijat u opcije
# Obrishi sve

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
allowed_option = ["dodaj","obrishi","izlistaj", "stop", "istorijat", "obrishi sve"]
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

            product_price = int(input("unesite cena proizvoda \n " ))

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

    elif option == "istorijat" :
        print(history)
        option = None
        
    elif option == "obrishi sve"
        products = {}
        option = None

print(products)












