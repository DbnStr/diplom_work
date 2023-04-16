import json


class Basket_item:
    def __init__(self, name, quantity, oneItemCost, amount):
        self.name = name
        self.quantity = quantity
        self.oneItemCost  = oneItemCost
        self.amount = amount

    def toJson(self):
        return json.dumps(self.__dict__)