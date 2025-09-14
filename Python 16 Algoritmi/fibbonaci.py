
#Fibbonaci znaci
#Saberi posledni 2 broja i dodaj

#Sabiraj do 100
# [0, 1]
#0+1=1, [0,1,1]
#1+1=2, [0,1,1,2]
#1+2=3, [0,1,1,2,3]
#2+3=5, [0,1,1,2,3,5].....

numbers = [0, 1]

while numbers [-1]< 100 :

    next_number = numbers[-1] + numbers[-2]

    if next_number > 100 :
        break
    numbers.append(next_number)
print(numbers)

