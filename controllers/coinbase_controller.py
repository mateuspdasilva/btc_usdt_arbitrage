# controllers/coinbase_controller.py
from services.coinbase_service import CoinbaseService

class CoinbaseController:
    @staticmethod
    def get_btc_price():
        return CoinbaseService.get_btc_price()
