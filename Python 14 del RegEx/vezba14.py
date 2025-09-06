
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
