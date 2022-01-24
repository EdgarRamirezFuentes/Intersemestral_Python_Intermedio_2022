import requests
import sys
from bs4 import BeautifulSoup

try:
    url ='https://ligamx.net'
    page_access = requests.get(url)
    # Get the HTML representation
    html = BeautifulSoup(page_access.content,'html.parser')
    # Get the links of the soccer teams
    teams_html = html.find_all('a','tpts loadershow col-xs-9 hidden-xs')
    # Cleaning the data to get the name of the soccer teams
    teams_list = [team.text.strip() for team in teams_html]
    for index, team in enumerate(teams_list):
        print(f"{index + 1}.- {team}")
except (requests.ConnectionError, requests.HTTPError):
    print(f"Connection to { url } failed")
    sys.exit(0)

