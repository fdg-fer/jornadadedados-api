import requests


def extrair_dados_bitcoin():
    url = 'https://api.coinbase.com/v2/prices/spot'
    resposta = requests.get(url)
    dados = resposta.json()
    return dados 

if __name__ == "__main__":
    print(extrair_dados_bitcoin())
    
    
    