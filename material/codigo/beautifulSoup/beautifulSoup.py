from socket import timeout
import requests
from bs4 import BeautifulSoup

page = requests.get('http://protecounam.mx/home', timeout=1)

variable_parse = BeautifulSoup(page.text, 'html.parser')

list_items = variable_parse.find_all('li')

# print(list_items)
# print(variable_parse)

for list_item in list_items:
    item_link = list_item.find_all('a')
    print(item_link[0].attrs.get('href'))


url = 'https://www.eldolar.info/es-MX/mexico/dia/hoy'

page = requests.get(url, timeout = 1)

parse_variable = BeautifulSoup(page.content, 'html.parser')

search = parse_variable.find_all('span', 'xTimes')

print(search)

