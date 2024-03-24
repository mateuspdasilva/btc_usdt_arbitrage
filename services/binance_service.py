# services/binance_service.py
import ccxt
from config.config import binance_api_key, binance_api_secret

class BinanceService:
    @staticmethod
    def get_btc_price():
        binance_client = ccxt.binance({
            'apiKey': binance_api_key,
            'secret': binance_api_secret,
        })
        ticker = binance_client.fetch_ticker('BTC/USDT')
        return ticker['last']
