#import requests
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def buscar_promocoes(produto):
    print("Escolha o tipo de busca:")
    print("1. Buscar em sites específicos")
    print("2. Buscar em várias fontes online")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        buscar_em_sites_especificos(produto)
    elif escolha == '2':
        buscar_em_varias_fontes(produto)
    else:
        print("Opção inválida.")

def buscar_em_sites_especificos(produto):
    # Configurando o webdriver do Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Para executar em modo headless (sem interface gráfica)
    driver = webdriver.Chrome(options=chrome_options)

    url = f"https://lista.mercadolivre.com.br/{produto}"
    driver.get(url)

    try:
        # Espera até 30 segundos para a página carregar
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'li')))
        resultados = driver.find_elements(By.XPATH, '//li[contains(@class, "ui-search-layout__item")]')

        if resultados:
            print("Promoções encontradas no Mercado Livre:")
            for resultado in resultados:
                titulo_elemento = resultado.find_element(By.XPATH, './/h2[contains(@class, "ui-search-item__title")]')
                
                # Procura por qualquer elemento contendo o texto "R$" dentro do contêiner do resultado
                preco_container = resultado.find_elements(By.XPATH, './/*[contains(text(), "R$")]')
                preco = preco_container[0].text.strip() if preco_container else "Preço não encontrado"
                
                titulo = titulo_elemento.text.strip()
                print(f"Produto: {titulo} | Preço: {preco}")
        else:
            print("Nenhuma promoção encontrada no Mercado Livre.")
    finally:
        driver.quit()

if __name__ == "__main__":
    produto = input("Digite o produto que deseja buscar promoções: ")
    buscar_em_sites_especificos(produto)

def buscar_em_varias_fontes(produto):
    # Implemente a busca em várias fontes online aqui
    print("Buscar em várias fontes online")

if __name__ == "__main__":
    produto = input("Digite o produto que deseja buscar promoções: ")
    buscar_promocoes(produto)
