#BUSCAR PREÇOS NA AMAZON.COM

from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.com.br/s?k='

nome = input('Qual produto deseja consultar? ')

response = requests.get(url + nome)

site = BeautifulSoup(response.text, 'html.parser')