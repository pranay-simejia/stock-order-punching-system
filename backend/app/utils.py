def calculate_quantity(amount_per_stock, stock_price):
    return amount_per_stock // stock_price

def get_available_slots(existing_stocks):
    return 20 - len(existing_stocks)

def filter_eligible_stocks(global_priority_list, existing_stocks):
    return [stock for stock in global_priority_list if stock not in existing_stocks]

def calculate_amount_per_stock(cash_remaining, slots):
    return cash_remaining / slots if slots > 0 else 0

def is_stock_affordable(amount_per_stock, stock_price):
    return amount_per_stock >= stock_price

def log_order(client_id, stock, quantity, status, message):
    return {
        "client_id": client_id,
        "stock": stock,
        "quantity": quantity,
        "status": status,
        "message": message
    }