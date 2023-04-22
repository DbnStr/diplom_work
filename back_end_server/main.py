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

    payment_link = REMOTE_ADDRESS + "/baskets/" + str(basket_id)
    response_body = {"paymentLink": payment_link}

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
        db.insert("ItemInBasket",
                  {
                      "quantity": el["quantity"],
                      "amount": el["amount"],
                      "basketId": basket_id,
                      "itemId": el["itemId"]
                  })
    return basket_id

@app.route("/baskets/<string:basket_id>", methods=['GET'])
def get_basket(basket_id):
    queries = request.args.to_dict()
    consumerId = int(queries.get('consumerId'))
    if consumerId != 'None':
        if user_exists(consumerId):
            basket = db.execute_select_one_query("SELECT * FROM Basket WHERE id = {}".format(basket_id))
            items_in_basket = db.execute_select_all_query("SELECT * FROM ItemInBasket WHERE basketId = {}".format(basket_id))
            resp_items = []
            for item_in_basket in items_in_basket:
                print(item_in_basket[4])
                item = db.execute_select_one_query("SELECT * FROM Item WHERE id = {}".format(item_in_basket[4]))
                resp_items.append({
                    "itemId": item[0],
                    "name": item[1],
                    "oneItemCost": item[2],
                    "quantity": item_in_basket[1],
                    "amount": item_in_basket[2]
                })
            resp = {
                "id": basket[0],
                "idInShop": basket[1],
                "shopId": basket[2],
                "consumerId": basket[3],
                "items": resp_items
            }
            db.update_one_record('Basket', {"consumerId": consumerId}, "consumerId = ".format(consumerId))
            return Response(json.dumps(resp), status=200, mimetype='application/json')
        else: print("User with consumerId = {} doesn't exist".format(consumerId))
    else:
        print("No user_id in request")

def user_exists(consumerId: int):
    return not db.execute_select_one_query("SELECT * FROM Consumer WHERE id = {}".format(consumerId)) is None

if __name__ == "__main__":
    app.run(debug=True, port=5002, host=REMOTE_HOST)