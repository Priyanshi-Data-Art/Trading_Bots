# validators.py

def check_side(side):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise Exception("Side must be BUY or SELL")
    return side


def check_order_type(order_type):
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise Exception("Order type must be MARKET or LIMIT")
    return order_type


def check_quantity(qty):
    if qty <= 0:
        raise Exception("Quantity must be greater than 0")
    return qty


def check_price(price, order_type):
    # price only required for LIMIT
    if order_type == "LIMIT" and int(price) <= 0:
        raise Exception("LIMIT order needs a valid price")
    return price