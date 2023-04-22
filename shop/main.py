import requests
from flask import Flask
import json

from Constants import *

from Basket import Basket
from Basket_item import Basket_item

app = Flask(__name__)

@app.route("/")
def hello_world():
    items = [Basket_item(1, 100, 1), Basket_item(1, 50, 2)]
    basket = Basket(1, 1, items)

    r = requests.post(REMOTE_URL     + "/baskets", json=basket.toJson())
    response_body = json.JSONDecoder().decode(r.text)

    print(response_body)
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True, port=5001)