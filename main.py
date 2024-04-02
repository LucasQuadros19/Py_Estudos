from bs4 import BeautifulSoup
import requests
import pandas as pd

lista=[] 
url = 'https://g1.globo.com'

response = requests.get(url)
content = response.content

site = BeautifulSoup(content, 'html.parser')

noticias = site.findAll('div', {'class': 'feed-post-body'})

for noticia in noticias:
    titulo = noticia.find('p', {'elementtiming': 'text-ssr'})

    resumo_div= noticia.find('div', {'class': 'feed-post-body-resumo'})
    if(resumo_div):
        resumo=resumo_div.find('p', {'elementtiming': 'text-ssr'})
        lista.append([titulo.text,resumo.text])
    else:
        lista.append([titulo.text])

news = pd.DataFrame(lista, columns=['Titulo','Resumo'])
news.to_excel('estudos.xlsx', engine='openpyxl', index=False)
