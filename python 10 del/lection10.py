
from methods import load_file, save_file

data = load_file("data/user.json")

print(data)

data.append({
        "name" : "test Test"
})
save_file("data/user.json", data)

