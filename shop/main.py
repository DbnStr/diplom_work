import requests
from flask import Flask, request, Response
import json

from Constants import *

from Basket import Basket
from Basket_item import Basket_item

app = Flask(__name__)

@app.route("/")
def hello_world():
    items = [Basket_item(1, 100, 1), Basket_item(1, 50, 2)]
    basket = Basket(1, 1, "http://194.87.99.230:5001/baskets/1", items, 150, 150)

    r = requests.post(REMOTE_BACK_END_SERVER_URL     + "/baskets", json=basket.toJson())
    response_body = json.JSONDecoder().decode(r.text)

    print(response_body)
    return "<p>Hello, World!</p>"

@app.route("/baskets/<int:basketId>", methods=['PATCH'])
def post_updated_basket(basketId):
    updated_basket = json.JSONDecoder().decode(request.json)
    print(updated_basket)
    return Response(status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True, port=5001, host=REMOTE_HOST)