# Svaka prodavanica ima svoje ime, svaka prodavnica ima svoje proizvode i njehove cene
# Napisati petlju koja ce ispisati sve cene hleba
shops = {
    "Maxi": {
        "hleb": 100,
        "novine": 50
    },
    "idea": {
        "hleb": 95,
        "novine": 62
    },
    "Izgrev": {
        "hleb": 120,
        "novine": 75
    },
    "FreeShp" : {
        "Novine" : 100
    },
    "Pijaca" : {
        "hleb" : 55
    }

}
# Total / kolicna
# Napisati petlju koja ce ispisati sve cene hleba
total_bread_price = 0
total_bread_shops = 0
max_bread_price = 0
max_bread_price_shop = ""


for shop_name, items in shops.items():
    if "hleb" in items :
      total_bread_price += items["hleb"]
      total_bread_shops += 1

      if max_bread_price < items ["hleb"] :
         max_bread_price = items["hleb"]
         max_bread_price_shop = shop_name



avarige_total_bread_price = total_bread_price / total_bread_shops
print(avarige_total_bread_price)
print(max_bread_price,max_bread_price_shop)

#ispisati koji ima naj vishoka cena


