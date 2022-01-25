import re

string = 'Buenos días grupo de Python Intermedio, espero que hayan descansado y que no tengan frío así como su servilleta'

# Return an span with the first coincidence
coincidences = re.search(r'grupo', string)

if coincidences:
    print('There are coincidences')
else:
    print('There are not coincidences')

# Return a list with all the coincidences
coincidences = re.findall(r'Python', string)

print(coincidences)

people = ['Fabián Josafat Díaz Silleros',
'Miriam Paola Sosa Toledo',
'Emma Belem Andrade Hernández',
'Carlos Ignacio Rodríguez Granados',
'Maria del Sol Silva Hernández',
'Isla Griselda Ponce Mendoza',
'Christopher Agustin Maya Guardado',
'César Rodrigo Méndez Hernández',
'Edgar Alejandro Ramírez Fuentes',
'José Iván Martínez Alvarado',
'Alejandro González Torres',
'Diego Armando Vivanco Quintanar',
'Esteban Flores',
'María Antonieta3',
'Edgar Navarro2',
'Martin Navarro',
'Miriam Cabello',
'Sofia Granados',
'Mario Vallarta']

for name in people:
    # Print the names that start with M
    if re.findall(r'^M', name):
        print(name)

for name in people:
    # Print the names that end with s
    if re.findall(r's$', name):
        print(name)

for name in people:
    # Print the names that start with any letter in the range from A to C uppercase
    if re.findall(r'^[A-C]', name):
        print(name)

for name in people:
    # Print the names that start with any letter in the range from a to c lowercase
    if re.findall(r'[a-c]$', name):
        print(name)
    
print(r'[1-31]')