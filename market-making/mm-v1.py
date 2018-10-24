from binance.client import Client
import os
client = Client(os.environ["BINANCE_ACCESS_KEY"], os.environ["BINANCE_ACCESS_SECRET_KEY"])

import time

while True:
    depth = client.get_order_book(symbol='BNBBTC')
    print(depth)
    time.sleep(1)
