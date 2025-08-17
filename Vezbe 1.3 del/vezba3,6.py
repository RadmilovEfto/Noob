# Vezba 2
# Pitajte korisnika sta zeli da uradi :
# A : Obrise proizvode (obrisati) -> izvrsiti logiku za brisanje
# B : Dodaj proizvod (dodaj) -> "test"

# Pitaj korisnika sta zeli da uradi :
# A : Obrisi -> Unesite ime proizvoda za brisanje -> brisemo proizvod
# B : Dodaj -> Unesite proizvoda i cenu -> "test"
products = {
    "hleb": {
        "cena": 100,
        "koicina": 50

    },
    "pivo": {
        "cena": 150,
        "kolicina": 220
    }

}

option = None
while option not in ["dodaj", "obrishi"]:
    option = input("Sta zelite da odradite [dodaj, obrishi]").lower()

if option == "obrishi":
    product = None

    while product not in products:
        product = input("Unesite ime proizvoda za brishenje : ").lower()

    del products[product]



elif option == "dodaj":

    product = None

    while product in products or product == None:
        product = input("Unesite ime proizvoda koje ne postoji: ")

    productPrice = None
    while productPrice == None or productPrice <= 0:
        productPrice = int(input("unesite cena proizvoda"))

    productAmaunt = None
    while productAmaunt == None or productAmaunt <= 0:
        productAmaunt = int(input("Unesite Kolicina prozivoda : "))

    products[product] = {
        "cena": productPrice,
        "koloicina": productAmaunt
    }

# kako da mi kada korisnik obrishe ili doda proizvod opet da ga pitamo sta zeli da uradi? vracamo korisnika na pocetak

print(products)












