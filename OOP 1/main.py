
# OOP
#Klasa
# Osoba -> ime , prezime, visina, tezina
  # Tomislav, Nikolic, 183.5, 100 -> Object <- toma = Person() : <- self
  # Marko, Markovic, 181.5, 120   -> Objekt
  # Sara, Petrovvic, 170, 70      -> Object
# Product -> name, size, prize, amount
# Kalssa moze imate atribute(variable), metode, def, funkcije


class Person :

    def __init__(self, name, age): #kada se kreira objekat mora da se prosledi ime
        self.name = name # to ime sto je prosledjeno vezujemo za taj objekat
        self.age = age

    def write_my_name(self):
        print(self.name, self.age)

efto = Person("Efto", 39)
efto.write_my_name()
toma = Person("toma", 35)
toma.write_my_name()
#Objekt
# Product -> name, size, prize, amount
# class Product -> "hleb" 123, 90, 1
# class Product -> 'kompir' 12, 123, 1