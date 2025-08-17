
#Pitati korisnika da unese ime proizvoda
#Kada unese ime proizvoda dodati proizvod u "kasu"
# Korisnik mora da uneti 3 proizvoda ukupno

kasa = list()
while len(kasa) < 3 :
    item = input("Unesite ime proizvoda : ")
    kasa.append(item)
    print(kasa)

# dok god  broj stavki u kasa je manji od 3 pitati korisnika da unese novi
# kada korisnik unese novi, dodati ga kasa
