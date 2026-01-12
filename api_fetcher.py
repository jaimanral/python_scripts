import requests

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def fetch_bitcoin_price():
    response = requests.get(URL)
    data = response.json()
    price = data["bpi"]["USD"]["rate"]
    print(f"Bitcoin price in USD: {price}")

if __name__ == "__main__":
    fetch_bitcoin_price()
