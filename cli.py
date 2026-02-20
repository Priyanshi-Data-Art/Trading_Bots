from bots.orders import price_limit_order, market_order
from bots.logging import setup_logging

setup_logging()

market_order = market_order("BTCUSDT", 0.002, "BUY")


limit_order = price_limit_order("BTCUSDT", 0.002, "SELL", "70000")
