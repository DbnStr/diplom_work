import json


class Basket_item:
    def __init__(self, quantity, amount, itemId):
        self.quantity = quantity
        self.amount = amount
        self.itemId = itemId

    def toJson(self):
        return json.dumps(self.__dict__)