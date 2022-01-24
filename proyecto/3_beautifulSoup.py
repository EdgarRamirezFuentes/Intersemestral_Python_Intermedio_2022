'''
    Name: 3_beautifulSoup.py
    Description: Get cars information using web scraping
    Author: Edgar Alejandro Ramírez Fuentes
    Date: 01/23/2021
'''

import requests
import sys
import re
from bs4 import BeautifulSoup

try:
    url = 'https://www.kavak.com/comprar-Chevrolet/tipo-hatchback/precio-93182-min/compra-de-autos'
    page_access = requests.get(url)
    # Get the HTML representation
    html = BeautifulSoup(page_access.content,'html.parser')
    cars_cards = html.find_all('div', 'card-body')
    print("Recommendations:\n")
    for car_card in cars_cards:
        # Getting the car name based on the HTML tags info
        car_name = car_card.find('h2', 'car-name').text.strip()
        # Cleaning the obtained data and getting the car year based on the HTML tags info
        car_year = int(car_card.find('p', 'car-details').text.strip().split(' ')[0])
        # Cleaning the obtained data and getting the car price based on the HTML tags info
        car_price = float(re.sub(',', '.', car_card.find('span', 'payment-highlight payment-total').text.strip()[1:]))
        # Check if the car model is Sonic
        pattern = re.compile('Sonic', flags=re.I)
        is_sonic = pattern.search(car_name)
        # Print the car recommendation only if it fulfill the requirements
        if not is_sonic and car_price < 220_000 and car_year > 2017:
            print(f'Car model: { car_name }\nYear: { car_year }\nPrice: ${ car_price }', end="\n---------------\n")
        
except (requests.ConnectionError, requests.HTTPError):
    print(f"Connection to { url } failed")
    sys.exit(0)
except Exception as e:
    print(e)
    sys.exit(0)
