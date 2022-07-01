

class QuantityType:
    NEW = 0
    EXPIRED = 1
    INVENTORY = 2

    QUANTITY_TYPE_CHOICES = (
        (NEW, 'New'),
        (EXPIRED, 'Expired'),
        (INVENTORY, 'Inventory')
    )

    QUANTITY_TYPE_DICT = dict(QUANTITY_TYPE_CHOICES)
