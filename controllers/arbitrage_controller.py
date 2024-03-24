# controllers/arbitrage_controller.py
from services.arbitrage_service import ArbitrageService

class ArbitrageController:
    @staticmethod
    def make_arbitrage():
        return ArbitrageService.make_arbitrage()
