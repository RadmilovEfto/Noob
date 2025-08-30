
import json


# Budzet
# Dodavanje troskova
# brisanje troskova
# logovanje troskova

user = None
maxi_buget = 1000000
with open('data/user.json', 'r') as file :
    user = json.load(file)

user_buget = user["buget"] + user["credit"]


print(user_buget) # buget + credit

if user_buget >= maxi_buget or user_buget <= 0 :
    print('Desila se greshka, vash buget je veci od dozvolenog ili je premali')
    exit()
print(f"vash budget iznosi  {user_buget} ")

expense = 0


while expense <= 0 or expense > user_buget :
    expense = int(input("Molim Vnesite iznos troshka :  "))

with open("logs/expense_log.txt", 'a') as file :
    remaining_budget = user_buget-expense
    message = f" \n Amaunt : {expense}, User : {user["id"]}, Buged : {user_buget}, Preostali buget {remaining_budget}"
    file.write(message)




#napravite tex file expens log.txt
#upisite svaki troshak u sledecem format
#"Amaunt : Cifra
