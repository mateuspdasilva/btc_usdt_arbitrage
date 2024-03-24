# services/coinbase_service.py
import requests

class CoinbaseService:
    @staticmethod
    def get_btc_price():
        response = requests.get('https://api.pro.coinbase.com/products/BTC-USDT/ticker')
        ticker = response.json()
        return float(ticker['price'])
