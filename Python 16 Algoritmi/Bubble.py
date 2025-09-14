
#BubbleSort
#Sortira stvari (elimenti)
#Uperedzuje
#Swap (menjanje)
#Multiple Passes - radi sve dok ne zavrshi te prve 2 akcije

numbers = [5,1,4,2,8]

numbers_length = len(numbers) #5

for i in range(numbers_length) :
    swapped = False

    for j in range(0, numbers_length-i-1) :
        if numbers[j]>numbers[j+1] :
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            swapped = True

    if not swapped :
        break

print(numbers)


