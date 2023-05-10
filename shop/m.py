from flask import Flask, render_template, request, session, redirect, url_for
import qrcode

from Constants import LOCAL_HOST

app = Flask(__name__)
app.secret_key = "super secret key"

app.config['items'] = [
    {"id": 1, "name": "Item 1", "price": 10},
    {"id": 2, "name": "Item 2", "price": 20},
    {"id": 3, "name": "Item 3", "price": 30},
    {"id": 4, "name": "Item 4", "price": 40},
]

app.config['cart'] = []

@app.route("/")
def index():
    return render_template("index.html", items=app.config['items'])

@app.route("/add_to_cart/<int:item_id>", methods=['GET'])
def add_to_cart(item_id):
    for item in app.config['items']:
        if item["id"] == item_id:
            app.config['cart'].append(item)

    print(app.config['cart'])
    return redirect(url_for("index"))

@app.route("/cart", methods=['GET'])
def cart():
    cart = app.config['cart']
    total = sum([item["price"] for item in cart])
    print(cart)
    return render_template("cart.html", items=cart, total=total)

@app.route("/clear_cart")
def clear_cart():
    app.config['cart'] = []
    return redirect(url_for("index"))

@app.route('/payment', methods=['GET'])
def payment():
    data = "http://194.87.99.230:5002/baskets/{}".format(1)
    img = qrcode.make(data)
    img.save('static/img/qr.png')
    return render_template('payment.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001, host=LOCAL_HOST)

