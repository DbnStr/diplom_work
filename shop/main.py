import requests
from flask import Flask, request, Response
import json
import bes_urls

from Constants import *

from Basket import Basket
from Basket_item import Basket_item

app = Flask(__name__)
urls = bes_urls.BES_Urls()

@app.route("/")
def hello_world():
    items = [Basket_item(1, 100, 1), Basket_item(1, 50, 2)]
    basket = Basket(1, 1, "{}/baskets/{}".format(REMOTE_URL, 1), items, 150, 150)

    r = requests.post(urls.get_url_for_posting_basket(), json=basket.toJson())
    response_body = json.JSONDecoder().decode(r.text)

    print(response_body)
    return "<p>Hello, World!</p>"

@app.route("/sendUpdatedBasket")
def send_updated_basket_with_local_discounts():
    r = requests.patch(urls.get_basket_location_url(1), json=json.dumps({
        "totalAmountWithDiscounts": 100
    }))
    return "<p>Hello, World!</p>"

@app.route("/baskets/<int:basketId>", methods=['PATCH'])
def post_updated_basket(basketId):
    updated_basket = json.JSONDecoder().decode(request.json)
    print(updated_basket)
    return Response(status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True, port=5001, host=REMOTE_HOST)