
# Ako korisnik unese bilo sta manje od 0, ispisi greshku i zaustavi program!


user = int(input("Unesite Godine : "))

if user < 0:
    print("Godine ne mogu biti maje od 0")
    quit()

if user  <= 12 :
    print("Vi ste dete ")
elif user >= 13 and user <= 17:
    print("Vi ste tinejdzer")
elif user >= 18 and user <= 64 :
    print("Vi ste odrasla osoba")
elif user >= 65:
    print("Vi ste penzioner")
else :
    print("Uneli ste pogreshni godine ili Vi niste uneli podatak ispravno")
