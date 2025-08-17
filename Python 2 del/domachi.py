#Napravi dicrionary koji ima sledecu strukturu :
# person1 : "name " : "Toma", "last_name " : "Nikolic",
# person2 : "name" : "Petar", "last_name" : "Pavlovic",
# person3 : "name" : " Mihajlo" , "last_name" : "Folic"

people = {
 "person": {
    "name" : "Toma",
    "last_name" : "Nikolic"
 },
 "person2" : {
    "name" : "Petar",
    "last_name" : "Pavlovic"
 } ,
 "person3" : {
    "name" : "Mihajlo",
    "last_name" : "Folic"
 }
}
print(people["person3"]["last_name"], people["person"] ["name"])