from .client import client_connection
from .validators import check_side, check_order_type, check_quantity, check_price
import logging


client=client_connection()

def logger(order):
    info = {
        "orderId": order.get("orderId"),
        "symbol": order.get("symbol"),
        "side": order.get("side"),
        "type": order.get("type"),
        "quantity": order.get("origQty"),
        "price": order.get("price"),
        "executedQty": order.get("executedQty"),
        "avgPrice": order.get("avgPrice"),
        "status": order.get("status")
    }
    logging.info(info)



def market_order(symbol,quantity,side):
    try:
        side = check_side(side)
        qty = check_quantity(quantity)

        order=client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=qty
        )

        print("Market Order Successfully Placed")
        logging.info("Market Order Details")
        logger(order)
        return order
    except Exception as e:
        print("Market Order failed")
        logging.error(str(e))
        return str(e)
    
def price_limit_order(symbol,quantity,side,price):
    try:
        side = check_side(side)
        qty = check_quantity(quantity)
        price = check_price(price, "LIMIT")
    
        order=client.futures_create_order(
            symbol=symbol,
            quantity=qty,
            side=side,
            type="LIMIT",
            price=price,
            timeInForce="GTC"
        )
        print("Limit Order Succesfully Placed")
        logging.info("Limit Order Details")
        logger(order)
    except Exception as e:
        print("Limit Order failed")
        logging.error(str(e))
        return str(e)

