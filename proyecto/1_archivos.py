import json

# Creating the assistants list
assistants = [
    {
        'name' : 'Edgar Ramirez',
        'age' : 23,
        'email' : 'edgar.ramirez.fuentes.dev@gmail.com',
        'origin' : {
            'name' : 'externo',
            'location' : ''
        },
        'courses' : {
            'Python Intermedio AM' : {
                'status' : 'en curso',
                'shift' : 'matutino' 
            }, 
            'Ciberseguridad' : {
                'status' : 'en curso',
                'shift' : 'vespertino' 
            }, 
            'Redes de Computadoras' : {
                'status' : 'en curso',
                'shift' : 'matutino' 
            }
        },
        'payment' : {
            'status' : True,
            'mount' : 1200.00,
            'date' : '14/01/2022'
        }
    },
    {
        'name' : 'Ivan Martinez',
        'age' : 23,
        'email' : 'ivan.martinez@gmail.com',
        'origin' : {
            'name' : 'externo',
            'location' : ''
        },
        'courses' : {
            'Python Intermedio AM' : {
                'status' : 'en curso',
                'shift' : 'matutino' 
            }, 
            'Ciberseguridad' : {
                'status' : 'en curso',
                'shift' : 'vespertino' 
            }, 
            'Redes de Computadoras' : {
                'status' : 'en curso',
                'shift' : 'matutino' 
            }
        },
        'payment' : {
            'status' : True,
            'mount' : 1200.00,
            'date' : '14/01/2022'
        }
    }
]
# Convert from python to JSON
json_data = json.dumps(assistants, indent=4)

# Creating a JSON file
with open('data.json', 'w') as json_file:
    json_file.write(json_data)
