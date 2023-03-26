#Basket имеет ID и список товаров items
import json


class Basket:
    def __init__(self, id, items):
        self.id = id
        self.items = items
    def toJson(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__)