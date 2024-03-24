# services/kraken_service.py
import requests

class KrakenService:
    @staticmethod
    def get_btc_price():
        try:
            response = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
            response.raise_for_status()
            data = response.json()
            return float(data['result']['XXBTZUSD']['c'][0])
        except Exception as e:
            print(f"Erro ao obter preço na Kraken: {e}")
            return None
