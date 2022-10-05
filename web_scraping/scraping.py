import requests
from bs4 import BeautifulSoup



url= 'https://www.globo.com/?utm_source=barraGCOM'
response= requests.get(url)
html= BeautifulSoup(response.text, 'html.parser')


for texto in html.select('.headline__container '):
    t= texto.select_one('.post__link')
    d= texto.select_one('.post__title')



    print(t, t.text, sep='\t')