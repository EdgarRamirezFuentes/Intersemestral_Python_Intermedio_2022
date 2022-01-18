'''
    Name: 2.py
    Description: It reads the data contained in a CSV file, and displays a specific data.
    Author: Edgar Alejandro Ramírez Fuentes
    Date: 01/17/2021
'''

import csv
import sys
try:
    # Getting the data from the CSV file
    with open('../files/csv_file.csv', 'r') as file:
        # Storing the data in a csv object
        data = csv.reader(file)
        # Storing the name of each champion
        champions = [champion[0] for champion in data]
        # Listing the champions
        for name in champions:
            print(name)
except FileNotFoundError as e:
    print(e)
    sys.exit(0)
