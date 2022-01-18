from base64 import encode
import csv

with open('csv_file.csv', encoding='utf-8') as file:
    data = csv.reader(file)
    
print(data)

