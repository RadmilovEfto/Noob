import re


name = "Tomislav Nikolic"

           # AB
pattern = r"^[A-Z][a-z]+ [A-Z][a-z]+$"

if re.match(pattern, name) :
    print("Ime i Prezime ")

