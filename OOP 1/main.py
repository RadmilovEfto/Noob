
# OOP
#Klasa
# Osoba -> ime , prezime, visina, tezina
  # Tomislav, Nikolic, 183.5, 100 -> Object <- toma = Person() : <- self
  # Marko, Markovic, 181.5, 120   -> Objekt
  # Sara, Petrovvic, 170, 70      -> Object
# Product -> name, size, prize, amount
# Kalssa moze imate atribute(variable), metode, def, funkcije


class Person :

    def __init__(self, name, age):
        print (name, age)

    def say_hello(self):
        print("Hello Wrold")

toma = Person("Efto", 39)
toma.say_hello()


#Objekt
# Product -> name, size, prize, amount
# class Product -> "hleb" 123, 90, 1
# class Product -> 'kompir' 12, 123, 1