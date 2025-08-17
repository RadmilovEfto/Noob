# array (listu) studentata
# svaki student : name "Toma" score : 0-100 active true false ->dictionary


students = [
    {
        "name" : "Toma",
        "score" : 99,
        "active" : True

    },
    {   "name" : "Marija",
        "score" : 66,
        "active" : True

    },
    {   "name" : "Toma",
        "score" : 29,
        "active" : True

    }
]

for student in students :
    if not student ["active"] :
        continue
    if student ["score"] >= 80 :
        student ["grade"] = "A"
    elif student ["score"] >60 < 79 :
        student ["grade"] = "B"
    elif student ["score"] > 40 < 59 :
        student ["grade"] = "C"
    elif student ["score"] > 21 < 39 :
        student ["grade"] = "D"
    else :
        student ["grade"] = "F"
print(students)






#napisite petlju koj ispisuje samo ucenike koji su aktivini
#Hint for, if
# ako ostavimo tako to je isto kao da sumo napishali if student["active"] == True:
# ako je skor studenta (ovo vazi samo za aktivni studenti )
# od 80 do 100 grade : A
# od 60 do 80 Grade B
# od 40 do 60 grade : C
# od 20 do 40 grade : D
# od < 20 grade : F




