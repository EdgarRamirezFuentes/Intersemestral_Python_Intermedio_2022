'''
    Name: 6_regex.py
    Description: Use Regular expressions to find required information and validate data
    Author: Edgar Alejandro Ramírez Fuentes
    Date: 01/25/2021
'''

import re

# Regex 1
name_regex = r'My\sname\sis\s([a-z]+)'

# Trigger My name is
text = '''- Hello, My name is Alejandro. What's your name? 
- Hi, my name is Edgar.
- Nice to meet you, Edgar.
- Nice to meet you too, Alejandro.
- Let me introduce my best friend Yael.
- Hi, Edgar. My name is Yael.
'''

names = re.findall(name_regex, text, flags=re.I)
print('Names found in the text: ')
for index, name in enumerate(names):
    print(f'{index + 1}.- {name}')

print('------------------')

# Regex 2
pattern = r'^[A-Z]{2}[1-9]{4}\-[a-z][0-9]$'

tests = ['AB1234-f0', 'NK1501-a2']
for test in tests:
    print(f'{test} is', ('valid' if re.match(pattern, test) else 'not valid'))

print('------------------')

# Regex 3
pattern_steel = r'acero'
text = '''Entonces el desconocido saludó mientras el vivo acero se
enfriaba a altas temperaturas. Nuestro campeón recordó sus días
de herrero donde de igual forma trabajó con acero, no pudiendo
observar los errores del desconocido al trabajar con acero, pues
su acero era de mala calidad y para empeorar las cosas, dicho
acero estaba siendo mal enfriado y martillado. Cualquier maestro
herrero del acero hubiera quedado horrorizado al ver semejante
trato y calidad de dicho acero.
'''
print(f'The word "acero" appears {len(re.findall(pattern_steel, text, flags=re.I))} times in the text')