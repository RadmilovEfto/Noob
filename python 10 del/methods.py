

import json

def load_file(file_name) :
    with open (file_name, 'r') as file :
        products = json.load(file)
        return products

def save_file(file_name, data) :
    with open (file_name, 'w') as file :
        json.dump(data, file, indent=4 )


