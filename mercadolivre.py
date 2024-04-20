from bs4 import BeautifulSoup
import requests

url = 'https://lista.mercadolivre.com.br/'

nome = input('Qual produto deseja consultar? ')

response = requests.get(url + nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16 andes-card--animated'})

for produto in produtos:

    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})

    link = produto.find('a', attrs={'class': 'ui-search-link'})

    preco = produto.find('span', attrs={'class': 'andes-money-amount__fraction'})

    #print(produto.prettify())
    print('Titulo do produto: ', titulo.text)
    print('Preço do produto: ', preco.text)
    print('Link do produto: R$', link['href'])

    print('\n\n')