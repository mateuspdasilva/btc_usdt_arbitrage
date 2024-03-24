# main.py
import time
from controllers.arbitrage_controller import ArbitrageController

def main():
    while True:
        arbitrage = ArbitrageController.make_arbitrage()
        print(arbitrage)

if __name__ == "__main__":
    main()
