import platform


pyt_version = platform.python_version()
print(f'Ova je tvoja verzija Python : {pyt_version}')

version = int(pyt_version[0])

if version != 3 :
    print ('Ne koristite pravilnu verziju na Python')
else :
    print("Welcome to Python coding ! ")



