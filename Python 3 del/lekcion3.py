

name = "Toma"

# ako je ime Toma -> ispishi poruku "Pozdrav Toma"
# ako je ime neko drugo ( ako nije Toma) ispishi "Pozdrav neko drugi"

# if (ako) name (je ime) == (ako je njegova vrednost ) "toma"
# ako je name "Toma"

if name == "Toma" :
    print("Pozdrav Toma")
    print("Pozdrav dugi put!")
else :
    print("Pozdrav neki drugo")

# vezba
# Uradite proberu, ako korisnik ima vise od 18 godina, ispisi "Punoletni ste"
# Ako korisnik ima manje od 18 godina ispisati "Niste punoletni"
age = 38
allowed_age = 18

# if 31>=18

if age >= allowed_age :
    print("Punoletni ste ! ")
else :
    print("Maloletni ste ! ")

age_difference = age - allowed_age
# 38-18 = 20
print(f"korisnik ima vishe od {age_difference} godina razlike")

# ako je ime admin          -> if
# ako je ime Toma           -> elif (elseif)
#ako je bilo koje ime       ->  else







