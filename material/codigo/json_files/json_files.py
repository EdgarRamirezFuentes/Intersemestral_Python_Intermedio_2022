import json

with open('./json_file.json', 'r') as file:
    data = json.load(file)
    print(data)