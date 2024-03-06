from collections import namedtuple
from decimal import Decimal

MAX_TOTAL = 1e6 # maximum total amount accepted for an order

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    payments = Decimal(0.0)
    expenses = Decimal(0.0)

    for item in order.items:
        # amountとquantityをDecimalに変換
        amount = Decimal(str(item.amount))
        quantity = Decimal(str(item.quantity))

        if item.type == 'payment':
            payments += amount
        elif item.type == 'product':
            expenses += amount * quantity
        else:
            return "Invalid item type: %s" % item.type

    if abs(payments) > MAX_TOTAL or expenses > MAX_TOTAL:
        return "Total amount payable for an order exceeded"

    if payments != expenses:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payments - expenses)
    else:
        return "Order ID: %s - Full payment received!" % order.id