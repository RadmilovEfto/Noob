#Napishite program koji trazi od korisnika da unese ime proizvoda, a zatim ispiujte cenu tog proizvoda,
# Ako proizvod ne postoji, ispisite poruku " Proizvod nije pronadzen.

products = {"iphone 14" : 500, "iphone 15" : 800, "samsung s23" :1000}

search_products = input("Unesete proizvod : ").lower()

# Vezba : Proveri dali postoji proizvod, dodati da se ime proizvoda izvlaci iz inputa, ispisite cenu proizvoda

if search_products in products:
    print(products[search_products])
else:
    print("Proizvod nije pronadzen! ")
