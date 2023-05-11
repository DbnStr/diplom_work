import datetime
from urllib import response

import requests
from flask import Flask, render_template, redirect, url_for, request, Response, jsonify
import json
import qrcode

import bes_urls
from models.Basket import Basket
from models.Basket_item import Basket_item
from models.Item import Item
from Constants import LOCAL_HOST, SHOP_ID, REMOTE_HOST

app = Flask(__name__)
urls = bes_urls.BES_Urls()
app.secret_key = "super secret key"

app.config['items'] = {
    1: Item(1, "Coca cola 1.5l", 100),
    2: Item(2, "Orbit Mint Gum", 50)
}
app.config['cart'] = {}


@app.route("/")
def index():
    app.config["user_scanned_qr"] = False
    app.config['invoice_is_paid'] = False
    return render_template("index.html", items=app.config['items'])


@app.route("/add_to_cart/<int:item_id>", methods=['GET'])
def add_to_cart(item_id):
    items = app.config['items']
    if item_id in items:
        cart = app.config['cart']
        if item_id not in cart:
            cart[item_id] = 1
        else:
            cart[item_id] = cart[item_id] + 1

    return redirect(url_for("index"))


@app.route("/cart", methods=['GET'])
def cart():
    cart_items = []
    cart = app.config['cart']
    for k in cart.keys():
        item = app.config['items'][k]
        item_quantity = cart[k]
        cart_items.append(
            Basket_item(
                item_quantity,
                item.cost * item_quantity,
                k
            ))
    total_amount = sum([i.amount for i in cart_items])
    app.config["basket_for_posting"] = get_basket_for_posting(cart_items, total_amount)
    return render_template("cart.html", items=cart_items, total=total_amount)

@app.route("/clear_cart")
def clear_cart():
    app.config['cart'] = {}
    return redirect(url_for("index"))


@app.route('/payment', methods=['GET'])
def payment():
    basket = app.config["basket_for_posting"]
    r = requests.post(urls.get_url_for_posting_basket(), json=basket.toJson())
    response_body = json.JSONDecoder().decode(r.text)

    data = response_body["paymentLink"]
    generate_qr_code(data)
    return render_template('payment.html')

# @app.route("/sendUpdatedBasket")
# def send_updated_basket_with_local_discounts():
#     r = requests.patch(urls.get_basket_location_url(1), json=json.dumps({
#         "totalAmountWithDiscounts": 100
#     }))
#     return "<p>Hello, World!</p>"

@app.route("/baskets/<int:basketId>", methods=['PATCH'])
def update_basket(basketId):
    updated_fields = json.JSONDecoder().decode(request.json)
    basket = app.config['basket_for_posting']
    basket.consumerId = updated_fields["consumerId"]
    basket.loyaltyId = updated_fields["loyaltyId"]
    basket.totalAmountWithDiscounts = updated_fields["totalAmountWithDiscounts"]

    print(basket)

    app.config["user_scanned_qr"] = True

    return Response(status=200, mimetype='application/json')

@app.route("/is_user_scanned")
def is_user_scanned():
    if app.config["user_scanned_qr"]:
        return jsonify(status=200)
    else:
        return jsonify(status=404)


@app.route("/is_invoice_paid")
def is_invoice_paid():
    if app.config['invoice_is_paid']:
        return jsonify(status=200)
    else:
        return jsonify(status=404)


@app.route("/payment_waiting")
def payment_waiting():
    send_invoice()
    return render_template("payment_waiting.html")


@app.route("/payment_success")
def payment_success():
    return render_template("payment_success.html")


@app.route("/payments", methods=['POST'])
def post_new_payment():
    app.config['invoice_is_paid'] = True
    return jsonify(status=201)


def send_invoice():
    basket = app.config['basket_for_posting']
    invoice = {
        "amount": basket.totalAmountWithDiscounts,
        "paymentMethods": "SBP, MIR",
        "expiredDateTime": (datetime.datetime.now() + datetime.timedelta(days=10)).isoformat(),
        "basketId": 1,
        "consumerId": basket.consumerId,
        "shopId": SHOP_ID
    }
    app.config['invoice'] = invoice
    r = requests.post(urls.get_url_for_posting_invoice(), json=json.dumps(invoice))
    print(json.JSONDecoder().decode(r.text))


def generate_qr_code(data: str):
    img = qrcode.make(data)
    img.save('static/img/qr.png')


def get_basket_for_posting(cart_items, total_amount: float):
    total_amount_with_discounts = total_amount * 0.9
    basket_for_posting = Basket(1, SHOP_ID, "http://194.87.99.230:5001/baskets/1", cart_items, total_amount, total_amount_with_discounts)
    return basket_for_posting


if __name__ == "__main__":
    app.run(debug=True, port=5001, host=REMOTE_HOST)
