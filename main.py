import requests
from bs4 import BeautifulSoup

# Hacemos la solicitud a la página web de Amazon
url = 'https://www.underarmour.fr/fr-fr/c/hommes/ua-hovr/'
response = requests.get(url)

# Parseamos el contenido HTML de la página con BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Encontramos todos los elementos HTML que contienen los productos en la página
products = soup.find_all('div', {'class': 'b-tile-info'})
print(len(products))
# Iteramos a través de los elementos para obtener información de cada producto
for product in products:
    # Encontramos el título del producto
    title = product.find('a', {'class': 'b-tile-name'}).text
    # Encontramos el precio del producto
    price = product.find('span', {'class': 'b-price-value'}).text
    # Imprimimos la información del producto
    print(title)
    print(price)
    print(' ')
