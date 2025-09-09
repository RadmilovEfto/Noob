import re


#[a-zA-Z]{1,5} to znaci da e ok t, to, tom, toma, tomaa.
#\d{2,} znaci nadzi 2 ili vishe broja zaredom

username = "toma1993"

pattern_name = r"[a-zA-Z]{1,5}\d{2,}"

match = re.match(pattern_name, username)

if match :
    print(match.group())