# config/config_example.py
import os

# Binance
binance_api_key = os.getenv('your_api_key')
binance_api_secret = os.getenv('your_api_scret')

SUPPORTED_EXCHANGES = ['binance', 'coinbase', 'kraken'] 