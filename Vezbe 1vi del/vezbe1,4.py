# Vezba 1 :
#Napravi lista proizvoda i ubaci 3 proizvoda IPhone 14, Iphone 15, Samsung S23.
# Napisi proveru koja proverava dali postoi "Iphone 14 u nashoj listi proizvoda


products = ["IPhone 14","IPhone 15","Samsung s23"]


# napravi zasebnu varijablu za ono sto trazimo

search_item = input("Enter item to search for: ")
print(search_item)
if search_item in products:
    print("IPhone 14 je u nashoj listi")
else :
    print("Nije IPhone 14 u nashoj listi")

