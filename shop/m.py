from flask import Flask, render_template, request, session, redirect, url_for
import qrcode

from Constants import LOCAL_HOST

app = Flask(__name__)
app.secret_key = "super secret key"

app.config['items'] = {
    1: {
        "id": 1,
        "name": "Coca cola 1.5l",
        "cost": 100
    },
    2: {
        "id": 2,
        "name": "Orbit Mint Gum",
        "cost": 50
    }
}

app.config['cart'] = {}

@app.route("/")
def index():
    return render_template("index.html", items=app.config['items'])

@app.route("/add_to_cart/<int:item_id>", methods=['GET'])
def add_to_cart(item_id):
    items = app.config['items']
    if item_id in items:
        cart = app.config['cart']
        if item_id not in cart:
            cart[item_id] = 1
        else: cart[item_id] = cart[item_id] + 1

    return redirect(url_for("index"))

@app.route("/cart", methods=['GET'])
def cart():
    cart_items = []
    cart = app.config['cart']
    for k in cart.keys():
        item = app.config['items'][k]
        item_quantity = cart[k]
        cart_items.append({
            "name": item["name"],
            "total_amount": item["cost"] * item_quantity,
            "quantity": item_quantity
        })
    total = sum([i["total_amount"] for i in cart_items])
    return render_template("cart.html", items=cart_items, total=total)

@app.route("/clear_cart")
def clear_cart():
    app.config['cart'] = {}
    return redirect(url_for("index"))

@app.route('/payment', methods=['GET'])
def payment():
    data = "http://194.87.99.230:5002/baskets/{}".format(1)
    img = qrcode.make(data)
    img.save('static/img/qr.png')
    return render_template('payment.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001, host=LOCAL_HOST)

