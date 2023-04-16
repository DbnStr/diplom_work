from flask import Flask, request, Response
import json

from database import db
from Constants import *

app = Flask(__name__)

json_basket = None

@app.route("/baskets", methods=['POST'])
def post_new_basket():
    basket_from_shop = json.JSONDecoder().decode(request.json)
    basket_id = save_basket_to_database(basket_from_shop)

    payment_link = "http://127.0.0.1:5002/baskets/" + str(basket_id)
    response_body = {"payment_link": payment_link}

    print("success payment_link request")

    return Response(json.dumps(response_body), status=200, mimetype='application/json')

def save_basket_to_database(basket_from_request):
    basket_id = db.insert_one_entry_and_return_inserted_id(
        "Basket",
        {
            "idInShop": basket_from_request["idInShop"],
            "shopId": basket_from_request["shopId"]
        }
    )[0]

    for el in basket_from_request["items"]:
        db.insert("Item",
                  {
                      "name": el["name"],
                      "quantity": el["quantity"],
                      "oneItemCost": el["oneItemCost"],
                      "amount": el["amount"],
                      "basketId": basket_id
                  })
    return basket_id

@app.route("/baskets/<string:basket_id>", methods=['GET'])
def get_basket(basket_id):
    queries = request.args.to_dict()
    if queries.get('user_id'):
        basket = db.execute_select_one_query("SELECT * FROM Basket WHERE id == {}".format(basket_id))
        items = db.execute_select_all_query("SELECT * FROM Item WHERE basketId == {}".format(basket_id))

        resp_items = []
        for i in items:
            resp_items.append({
                "name": i[1],
                "quantity": i[2],
                "oneItemCost": i[3],
                "amount": i[4]
            })
        resp = {
            "id": basket[0],
            "idInShop": basket[1],
            "shopId": basket[2]
        }
        return Response(json.dumps(resp), status=200, mimetype='application/json')
    else:
        print("No user_id in request")

if __name__ == "__main__":
    app.run(debug=True, port=5002, host=LOCAL_HOST)