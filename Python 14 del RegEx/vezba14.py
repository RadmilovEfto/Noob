
 #Regex koji ce proveravati dali ima samo slova unatar stringa
import re



sentence = "I love Python"
letter_pattern = r"^[a-zA-Z ]+$"

if re.match(letter_pattern, sentence):
    print("Ima samo bukvi")
else :
    print("ima i broevi")



important_sentence = "Today will rain all day"

capital_pattern = r"^[A-Z]"


if re.match(capital_pattern,important_sentence) :
    print("String pocinje sa veliko slovo")
else :
    print("String Pocinje sa malo slovo")

phone_nummber = "06764238244"
# 0678, 0677, 0660,
phone_pattern = r"^067(6|7|0)"

phone_match = re.match(phone_pattern, phone_nummber)

phone_map = {
    "0676" : "Linz",
    "0677" : "Tirol",
    "0660" : "Salzburg"

}


if phone_match :
    prefix = "067"+phone_match.group(1)

    print(f"Prefix number is {prefix} and country is {phone_map[prefix]} ")