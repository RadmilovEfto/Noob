import re


# RegEx -> (regolarni expres) radmilov.efto@gmail.com -> rec@rec.rec.dodatak


# dali se ovde samo broevi
our_number = "12345"

# (malo slovo r) predstavlja da mi trazimo i tretiramo ceo string kao obican text
# \ escape character

# r = sve sto proveravam tretijar kao obican text
# ^ = trazimo od pocetka stringa
# \d = trazi samo brojeva (0-9) = matches any numbers from 0 to 9
# + da nastavi da trazi da prodolzi da trazi
# $ do kraja stringa

# Proveri dali su samo brojevi unutar necega
pattern = r"^\d+$"
# proveri dali postoi taj pattern (sablon) unatar strnga(our_numbers)
if re.match(pattern, our_number) :
    print("Vnatre se samo broevi")
else :
    print("Vante ne se samo broevi")





