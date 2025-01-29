import requests

def fetch_data():
    url = "https://api.dexscreener.com/latest/dex/tokens/TOKEN_ADDRESS"
    response = requests.get(url)
    data = response.json()
    return data
