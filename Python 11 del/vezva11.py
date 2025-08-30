
import json


# Budzet
# Dodavanje troskova
# brisanje troskova
# logovanje troskova

user = None
maxi_buget = 100000
with open('data/user.json', 'r') as file :
    user = json.load(file)

print(user['buget'])

if user['buget'] >= maxi_buget or user['buget'] <= 0 :
    print('Desila se greshka, vash buget je veci od dozvolenog ili je premali')
    exit()
print("vash bodget iznosi { user ['buget'] }")