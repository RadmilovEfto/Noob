
 #Regex koji ce proveravati dali ima samo slova unatar stringa
import re



sentence = "I love Python"
letter_pattern = r"^[a-zA-Z ]+$"

if re.match(letter_pattern, sentence):
    print("Ima samo bukvi")
else :
    print("ima i broevi")
