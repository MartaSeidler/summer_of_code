import requests
from bs4 import BeautifulSoup

source = requests.get('https://flynerd.pl/').text

soup = BeautifulSoup(source, 'html.parser')

# print(soup.prettify())

print(soup.title.text)
print()

n=1
for article in soup.find_all('article'):
  article_title = article.h3.text
  print("{}. {}".format(n, article_title))

  article_text = article.p.text
  print(article_text)
 
  print()
  n += 1

