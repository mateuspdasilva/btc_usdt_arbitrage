# controllers/kraken_controller.py
from services.kraken_service import KrakenService

class KrakenController:
    @staticmethod
    def get_btc_price():
        return KrakenService.get_btc_price()
