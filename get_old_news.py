import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news/archive/2023-02-12'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
headlines = []

for headline in soup.find_all('h3'):
    headlines.append(headline.text)

print("Titulares de noticias del 12 de febrero de 2023:")
for i, headline in enumerate(headlines, start=1):
    print(f"{i}. {headline}")
