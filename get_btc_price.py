import requests

def get_latest_crypto_price(coin):
    url = f'https://api.pro.coinbase.com/products/{coin}-usd/ticker'
    response = requests.get(url)
    response_json = response.json()
    price = float(response_json['price'])
    return price

bitcoin_price = get_latest_crypto_price('BTC')
print(f"The latest Bitcoin price is: ${bitcoin_price:.2f}")
