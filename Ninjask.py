import os
import platform
import time
import random
import requests
from requests.exceptions import RequestException


# Seleciona uma lista de países aleatórios
paises = ["United States", "Canada", "Argentina", "Mexico", "Costa Rica", "Chile", "Europe", "United Kingdom", "Germany",
          "Netherlands", "France", "Sweden", "Switzerland", "Belgium", "Denmark", "Norway", "Poland", "Ireland",
          "Czech Republic", "Italy", "Spain", "Finland", "Serbia", "Austria", "Slovakia", "Slovenia", "Bulgaria",
          "Hungary", "Latvia", "Romania", "Portugal", "Luxembourg", "Ukraine", "Greece", "Estonia", "Iceland",
          "Albania", "Cyprus", "Croatia", "Moldova", "Bosnia and Herzegovina", "Georgia", "North Macedonia",
          "Lithuania", "Asia Pacific", "Australia", "Singapore", "Japan", "Hong Kong", "New Zealand", "Taiwan",
          "Vietnam", "Indonesia", "Malaysia", "South Korea", "Thailand", "South Africa", "United Arab Emirates",
          "Israel", "Türkiye"]

# Define o tempo de espera em segundos
tempo_espera = 60

# URL do site a ser verificado
url = "https://threewordphrase.com/"

# Função para trocar de IP
def trocar_ip(pais):
    sistema_operacional = platform.system()

    if sistema_operacional == "Windows":
        os.chdir(r"C:\Program Files\NordVPN")
        os.system("nordvpn -d")
        os.system(f"nordvpn -c -g {pais}")
    elif sistema_operacional == "Linux":
        os.system("nordvpn disconnect")
        os.system(f"nordvpn connect {pais}")

# Faz um loop infinito
while True:
    # Conecta à VPN do país selecionado
    pais = random.choice(paises)
    trocar_ip(pais)

    # Verifica o status code a cada intervalo de tempo
    while True:
        # Faz a requisição HTTP para verificar o status code
        try:
            response = requests.get(url)
            status_code = response.status_code
        except RequestException as e:
            # Caso ocorra uma exceção na conexão, imprime o erro e continua o loop
            print(f"Erro na conexão: {e}")
            continue

        # Verifica o status code e faz a troca de IP, se necessário
        if status_code != 200:
            trocar_ip(pais)

        # Imprime o status code
        print(f"Status code: {status_code}")

        # Espera x segundos (definido anteriormente)
        time.sleep(tempo_espera)
