import re


with open('logs/http.log', 'r') as file :
    lines = file.readlines()

error_pattern = r'Error \d{3}'
success_pattern =r'Status \d{3}'

for line in lines :
    if re.search(error_pattern, line) :
        with open ("logs/errors.log","a") as errors_file :
            errors_file.write(line)

    elif re.search(success_pattern, line):
        with open ("logs/success.log","a") as success_file :
            success_file.write(line)



