import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20030404204900/http://www0.bbc.co.uk/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Asumiendo que los titulares están en etiquetas <a> con clase "headline"
    headlines = soup.find_all("a", class_="headline")

    # Crear una lista vacía para almacenar los titulares
    headlines_list = []
    
    for headline in headlines:
        headlines_list.append(headline.text.strip())

    # Imprimir los titulares en una lista con comillas y una coma al final de cada línea
    for index, headline_text in enumerate(headlines_list):
        print(f'"{headline_text}",')
else:
    print("No se pudo obtener la página.")
