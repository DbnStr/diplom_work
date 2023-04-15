import json


class Basket_item:
    def __init__(self, name, quantity, one_item_cost, amount):
        self.name = name
        self.quantity = quantity
        self.one_item_cost  = one_item_cost
        self.amount = amount

    def toJson(self):
        return json.dumps(self.__dict__)