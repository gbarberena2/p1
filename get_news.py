import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
headlines = []

for headline in soup.find_all('h3'):
    headlines.append(headline.text)

print("Titulares de noticias del día de hoy:")
for i, headline in enumerate(headlines, start=1):
    print(f"{i}. {headline}")
