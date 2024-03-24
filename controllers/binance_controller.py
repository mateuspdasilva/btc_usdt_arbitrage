# controllers/binance_controller.py
from services.binance_service import BinanceService

class BinanceController:
    @staticmethod
    def get_btc_price():
        return BinanceService.get_btc_price()
