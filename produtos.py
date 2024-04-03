import requests
from bs4 import BeautifulSoup
import os

os.system('clear')
url_base='https://lista.mercadolivre.com.br/guitarras#D[A:guitarras,L:undefined]'
pesquisa= "guitarra"   #input("Buscar produto:  ")

response=requests.get(url_base)
site = BeautifulSoup(response.text, 'html.parser')
produtos=site.findAll('div', {'class':'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16 andes-card--animated'})

for produto in produtos:
    titulo=produto.find('h2', { 'class':'ui-search-item__title'})

    print(titulo.text)
    print("  ")