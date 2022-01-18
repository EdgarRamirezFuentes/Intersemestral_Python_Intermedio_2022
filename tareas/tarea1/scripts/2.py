'''
    Name: 2.py
    Description: It reads the data contained in a JSON file, and displays a specific data.
    Author: Edgar Alejandro Ramírez Fuentes
    Date: 01/17/2021
'''
import json
import sys


# Getting the data from the JSON file
try:
    with open('../files/json_file.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError as e:
    print(e)
    sys.exit(0)
else:
    # Storing the members data
    try:
        members = data['members']
    except KeyError as e:
        print(f"The key {e} does not exist in the data.")
        sys.exit(0)
    else:
        try:
            # Getting only the name and their superpowers
            members = {member['name'] : member['powers'] for member in members}
        except KeyError as e:
            print("There was a problem trying to get the superpowers of a member.")
            sys.exit(0)
        else:
            print("Superheroes list\n")
            # Listing each hero and their superpowers.
            for name, superpowers in members.items():
                print(f'{name} superpowers: ')
                print("\t", end="")
                for superpower in superpowers:
                    print(superpower, end=" . ")
                print("")
finally:
    print("\nThanks for  using our superhero system.")



