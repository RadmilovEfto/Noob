
import json



with open("data/user.json", 'r') as file :
    data = json.load(file)
    print(data[0] ["name"])
    data.append({
        "name" : "Petar Mijatovic",
        "age" : 25,
        "height" : 185,
        "gender" : "male"

    })
    print(data)
with open("data/user.json", 'w') as file :
    json.dump(data,
              file,
              indent=1)
