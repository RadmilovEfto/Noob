import re

bonus_code = "ABC123, tom255, bonus455, bonus22"

# [A-Za-z]{3} -> pronajdi 3 bukci po red
#\d vaka terame broevi
#\d{3} baraj tri broja po red
#

pattern = r"\b[A-Za-z]{3}\d{3}"

product_code = re.findall(pattern, bonus_code)
print(product_code)