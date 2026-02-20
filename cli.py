from bots.orders import price_limit_order, market_order
from bots.logging import setup_logging

setup_logging()


symbol = input("Enter symbol (e.g., BTCUSDT): ")
side = input("Enter side (BUY/SELL): ")
quantity = float(input("Enter quantity: "))
order_type = input("Enter order type (MARKET/LIMIT): ")

if order_type.upper() == "MARKET":
    market_order(symbol, quantity, side)
else:
    price = input("Enter price for LIMIT order: ")
    price_limit_order(symbol, quantity, side, price)
