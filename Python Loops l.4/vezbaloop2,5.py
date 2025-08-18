# Pitaj korisnika kolko godina ima
# Ako nije uneo godine, pitaj opet

age = ""

while not age.isdigit() or int(age)< 18 :
    age = input("kolko godini imate : ")

    print(age)