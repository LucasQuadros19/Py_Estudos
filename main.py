from bs4 import BeautifulSoup
import requests

url = 'https://g1.globo.com'


response = requests.get(url)
content = response.content


site = BeautifulSoup(content, 'html.parser')


noticia = site.find('div',{'class': 'feed-post-body'}) 


print(noticia.prettify())
