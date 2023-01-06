from bs4 import BeautifulSoup
import requests
import json

# Variables that point to the website to scrape, and handle the request and response from the website
url = 'https://marvelsnap.io/database/characters/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the spans with class names given to create an empty list for cards
card_name = soup.findAll('span', attrs={"class":"figcap-card-name"})
card_ability = soup.findAll('span', attrs={"class":"figcap-card-ability"})
cards_list = []

# Loop through the span tags and append the card's name and ability to the list
for name, ability in zip(card_name, card_ability):
  cards_list.append({'Card Name': name.text, 'Card Ability': ability.text})

# Create a list of JSON strings from the list created above
cards_list_json = json.dumps(cards_list, indent=2)
print(cards_list_json)