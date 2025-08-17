from os import remove

products = {
    "hleb" : {
        "cena" : 100,
        "koicina" : 50

    },
    "pivo" : {
        "cena" : 150,
        "kolicina" : 220
    }

}
print(products)

#treba pirari korisnika (?) da unese ime proizvoda za bisanje!
# koj proizvod zelite da obrishete !
# Potencionalni Problemi :
# 1. Korisnik ne unse ime proizvoda stavi enter samo
# while petlja, dok korisnik ne unese proizvod koj imamo
# 2. Unese ime proizvoda a mi nemamo taj proizvod
# 3. Uneo je ime Proizvod sa veliki slovama


product = None
while product not in products :
    product = input("Unesite ime proizvoda za brishenje : ").lower()
    print("Product ne postoi ")
del products[product]
print(products)





