
name = "admin"
password = "mojaSifra"

#ako je ime admin I AKO je sifra mojaSifra
#Ako je ime "toma" i ako je sifra "123456" print(dobrodoshao admine)
#Ako je ime "Marija" i ako je sifra "654789" print(dobrodoshla Marija)
# else print "Niste administrator! Pogreshna sifra

if name == "admin" and password == "mojaSifra":
    print("Dobrodoshao Admine")
elif name == "admin" and password == "123456":
    print("Dobrodoshao Tomo")
elif name == "Marija" and password == "654789" :
    print("Dobrodoshla Marija")
else :
    print("Niste administator! Pogreshna sifra ili ime !")

