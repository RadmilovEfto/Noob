
# da proverime da li ova e e-mail.
import re
e_mail = "ramdilov.efto@gmail.com"


pattern = r"^[a-zA-Z0-9.-]+@[a-zA-Z]+\.[a-zA-Z]+$"


if re.match(pattern, e_mail )  :
    print ("E-mail is valid ! You can continue! ")
else :
    print("Not correct e-mail. Please try again ! ")


