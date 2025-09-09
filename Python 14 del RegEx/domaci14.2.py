# da proverime da li ova e e-mail.
import re

e_mail = "toma@gmail.com"

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

#proveri neki pre @ dali ima (slova.-)
#\w proveri dali postoi slova
# \ .- proveri dali postoi . ili -
# proveri dali sostoi [\w \.-] bukvi ili ovie znaci
# + prodolzuva, dali postoi @
#\. proveruvame da li postoi .
#\w dali imame nekoj teks poste tocka
#\w
# [\w \.-] -> toma
# +@       -> @
#[\w \.-]  ->gmail
# \.       -> .
#\w        -> com




if re.match(pattern, e_mail )  :
    print ("E-mail is valid ! You can continue! ")
else :
    print("Not correct e-mail. Please try again ! ")
