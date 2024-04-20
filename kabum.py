#SCRIPT PARA BUSCAR MENOR PREÇO




#PROBLEMAS NAS TAGS DE PREÇO E LINK
#SITE NÃO MOSTRA AS TAGS NA PÁGINA DE BUSCA





from bs4 import BeautifulSoup
import requests

url = 'https://www.kabum.com.br/busca/'

nome = input('Qual produto deseja consultar? ')

response = requests.get(url + nome)

site = BeautifulSoup(response.text, 'html.parser')

produto = site.find('div', attrs={'class': 'sc-8932d6e-11 hFmiAx'})

titulo = produto.find('span', attrs={'class': 'sc-d79c9c3f-0 nlmfp sc-8932d6e-16 feBisz nameCard'})

#link = produto.find('a', attrs={'class': ''})

#preco = produto.find('span', class_='sc-b1f5eb03-2 iaiQNF priceCard').get_text()

print(produto.prettify())
print('Titulo do produto: ', titulo.text)
#print('Preço do produto: ', preco)
#print('Link do produto: ', link)
