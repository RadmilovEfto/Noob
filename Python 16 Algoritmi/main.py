
# Sort, BubbleSort, Factorial, Calculation

#Linear Serach
#nadzi najveci broj u listi
#neka nam maximalni broj po defaultu bude prvi broj

# Predzi preko svi brojeva. ako je trenutni maximalni manji od broja iz petle
# onda je taj iz petlje maximalno broj


numbers=[3, 5, 2, 1 ,8, 12, 6, 4, 9]

max_number = numbers[0]

for number in numbers :
    if number > max_number :
        max_number = number
print(max_number)

#vezba Pronajdi broj 8

for number in numbers :
    if number == 8 :
        print("pronashli smo broj 8")
        break

#Nadzi kolko puta se ponavlja broj 8
# Nadzi kolko puta se nesto ponavlja iz array
# Proveri dulpikate

