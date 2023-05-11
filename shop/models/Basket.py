#Basket имеет ID и список товаров items
import json


class Basket:
    def __init__(self, idInShop, shopId, callbackURL, items, totalAmount, totalAmountWithDiscounts):
        self.idInShop = idInShop
        self.shopId = shopId
        self.callbackURL = callbackURL
        self.items = items
        self.totalAmount = totalAmount
        self.totalAmountWithDiscounts = totalAmountWithDiscounts

    def toJson(self):
        return json.dumps({
            "idInShop": self.idInShop,
            "shopId": self.shopId,
            "callbackURL": self.callbackURL,
            "items": self.items,
            "totalAmount": self.totalAmount,
            "totalAmountWithDiscounts": self.totalAmountWithDiscounts
        }, default=lambda o: o.__dict__)