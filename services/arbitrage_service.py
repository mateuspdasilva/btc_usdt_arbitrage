from config.config import SUPPORTED_EXCHANGES

class ArbitrageService:
    @staticmethod
    def make_arbitrage():
        prices = {}
        for exchange in SUPPORTED_EXCHANGES:
            controller_name = exchange.capitalize() + "Controller"
            try:
                controller_module = __import__('controllers.' + exchange + '_controller', fromlist=[controller_name])
                controller_class = getattr(controller_module, controller_name)
                price = controller_class.get_btc_price()
                prices[exchange] = price
            except Exception as e:
                print(f"Erro ao obter preço da {exchange.capitalize()}: {e}")
                prices[exchange] = None

        # Remove exchanges with None values
        prices = {k: v for k, v in prices.items() if v is not None}

        if not prices:
            return None, None, None, None, None, None

        highest_price_exchange = max(prices, key=prices.get)
        lowest_price_exchange = min(prices, key=prices.get)
        highest_price = prices[highest_price_exchange]
        lowest_price = prices[lowest_price_exchange]
        absolute_difference = highest_price - lowest_price
        percent_difference = (absolute_difference / lowest_price) * 100

        highest_with_name = f"Highest: USDT {highest_price} ({highest_price_exchange})"
        lowest_with_name = f"Lowest: USDT {lowest_price} ({lowest_price_exchange})"
        absolute_difference_str = f"Difference: USDT {absolute_difference}"
        percent_difference_str = f"Difference: {percent_difference}%"

        return highest_with_name, lowest_with_name, absolute_difference_str, percent_difference_str
