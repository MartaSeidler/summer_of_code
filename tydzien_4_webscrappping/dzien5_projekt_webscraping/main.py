import requests
import time
from bs4 import BeautifulSoup

#city = "Bydgoszcz"
city = input("Podaj miejscowość: ")

source = requests.get(f'https://www.meetup.com/pl-PL/find/?location=pl--{city}&source=EVENTS&distance=hundredMiles')

soup = BeautifulSoup(source.content, 'html.parser')

#print(soup.prettify())

count = 1
for n in soup.find_all('a', id="event-card-in-search-results"):
  print()
  print(30 * '* ')
  print()
  print(f"{count}. ")
  print(f"Wydarzenie: {n.h2.text}")
  print(f"Data: {n.h3.text}")
  print(f"Miejsce: {n.p.text[12:]}")
  print()
  count += 1
  time.sleep(5)
  
  link = n.get("href")
  source_2 = requests.get(link)
  soup_2 = BeautifulSoup(source_2.content, 'html.parser')
  print("Opis wydarzenia:")
  details = soup_2.find('div', id='event-details')
  print(details.text)
  time.sleep(5)

# zapisywanie do pliku

# obsługa błędów