from bs4 import BeautifulSoup
import requests
import json

url = 'https://marvelsnap.io/database/characters/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
card_name = soup.findAll('span', attrs={"class":"figcap-card-name"})
card_ability = soup.findAll('span', attrs={"class":"figcap-card-ability"})
cards_list = []

for name, ability in zip(card_name, card_ability):
  cards_list.append({'Card Name': name.text, 'Card Ability': ability.text})

cards_list_json = json.dumps(cards_list, indent=2)
print(cards_list_json)