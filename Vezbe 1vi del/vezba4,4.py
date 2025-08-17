
""" Korisnik treba da unese cena korpa
Ako je cena preku 1000 evra ispisati koliki popust su osvarili (10%) - 1000.
 "Ostvarili ste 10% popusta sto iznosi 100 evra
 Ako je cena ispod 1000 ispisati "Vase korpa iznosi 1000 evra
 1vo pritajte korisnik za negova ceva, 2ri racunaj porez Revidiram kod i proveravam dali to moze bolje
"""


price = int(input("Price your product : "))

if price >= 1000 :
    tax_amount = price * 0.10
    print(f"Ostavarili ste 10% popusta, sto ukopno iznosi {tax_amount} eura ")
else :
    print("Cena je manja 1000 evra ")



