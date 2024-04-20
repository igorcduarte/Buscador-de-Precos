#BUSCAR PREÇOS NA TERABYTESHOP.COM.BR

from bs4 import BeautifulSoup
import requests

url = 'https://www.terabyteshop.com.br/busca?'

nome = input('Qual produto deseja consultar? ')

response = requests.get(url + nome)

site = BeautifulSoup(response.text, 'html.parser')