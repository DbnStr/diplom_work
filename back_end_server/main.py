from flask import Flask, request, Response
import json

from database import db
from Constants import *
import requests

app = Flask(__name__)

json_basket = None

@app.route("/baskets", methods=['POST'])
def post_new_basket():
    basket_from_shop = json.JSONDecoder().decode(request.json)
    print(basket_from_shop)
    basket_id = save_basket_into_database(basket_from_shop)

    payment_link = REMOTE_ADDRESS + "/baskets/" + str(basket_id)
    response_body = {"paymentLink": payment_link}

    print("success payment_link request")

    return Response(json.dumps(response_body), status=200, mimetype='application/json')

@app.route("/baskets/<string:basketId>", methods=['GET'])
def get_basket(basketId):
    queries = request.args.to_dict()
    consumerId = int(queries.get('consumerId'))
    if consumerId != 'None':
        if user_exists(consumerId):
            db.update_one_record('Basket', {"consumerId": consumerId}, "id = {}".format(basketId))
            apply_discounts_to_basket(basketId, consumerId)

            basket = get_basket_for_consumer(basketId)
            send_updated_basket_to_shop(basketId)
            return Response(json.dumps(basket), status=200, mimetype='application/json')
        else:
            print("User with consumerId = {} doesn't exist".format(consumerId))
            return Response("User with consumerId = {} doesn't exist".format(consumerId), status=400, mimetype='application/json')
    else:
        print("No user_id in request")
        return Response("No user_id in request", status=400, mimetype='application/json')

@app.route("/baskets/<string:basketId>", methods=['PATCH'])
def update_basket(basketId):
    if basket_exists(basketId):
        totalAmountWithDiscounts = json.JSONDecoder().decode(request.json)["totalAmountWithDiscounts"]
        db.update_one_record("Basket", {"totalAmountWithDiscounts": totalAmountWithDiscounts}, "id = {}".format(basketId))
        return Response("Success", status=200, mimetype="application/json")
    else: return Response("Basket with basketId={} doesn't exist", status=400, mimetype="application/json")

@app.route("/invoices", methods=['POST'])
def post_new_invoice():
    invoice_from_shop = json.JSONDecoder().decode(request.json)
    print(invoice_from_shop)
    invoiceId = save_invoice_into_database(invoice_from_shop)

    print("Success invoice publication with id={}".format(invoiceId))

    response_body = {"invoiceId": invoiceId}
    return Response(json.dumps(response_body), status=200, mimetype='application/json')

def save_invoice_into_database(invoice_from_request):
    invoice_id = db.insert_one_entry_and_return_inserted_id(
        "Invoice",
        {
            "amount": invoice_from_request["amount"],
            "paymentMethods": invoice_from_request["paymentMethods"],
            "expiredDateTime": invoice_from_request["expiredDateTime"],
            "basketId": invoice_from_request["basketId"],
            "consumerId": invoice_from_request["consumerId"],
            "shopId": invoice_from_request["shopId"]
        }
    )[0]
    return invoice_id

def save_basket_into_database(basket_from_request):
    basket_id = db.insert_one_entry_and_return_inserted_id(
        "Basket",
        {
            "idInShop": basket_from_request["idInShop"],
            "callbackURL": basket_from_request["callbackURL"],
            "totalAmount": basket_from_request["totalAmount"],
            "totalAmountWithDiscounts": basket_from_request["totalAmountWithDiscounts"],
            "shopId": basket_from_request["shopId"],
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

def get_basket_for_consumer(basketId: int):
    basket = db.execute_select_one_query("SELECT * FROM Basket WHERE id = {}".format(basketId))
    items_in_basket = db.execute_select_all_query("SELECT * FROM ItemInBasket WHERE basketId = {}".format(basketId))
    resp_items = []
    for item_in_basket in items_in_basket:
        item = db.execute_select_one_query("SELECT * FROM Item WHERE id = {}".format(item_in_basket[4]))
        resp_items.append({
            "itemId": item[0],
            "name": item[1],
            "oneItemCost": item[2],
            "quantity": item_in_basket[1],
            "amount": item_in_basket[2]
        })
    return {
        "id": basket[0],
        "idInShop": basket[1],
        "totalAmount": basket[3],
        "totalAmountWithDiscounts": basket[4],
        "shopId": basket[5],
        "consumerId": basket[6],
        "items": resp_items
    }

def apply_discounts_to_basket(basketId, consumerId):
    totalAmount = db.execute_select_one_query("SELECT totalAmount FROM Basket WHERE id = {}".format(basketId))[0]
    db.update_one_record('Basket', {"totalAmountWithDiscounts": totalAmount * 0.9}, "id = {}".format(basketId))

def send_updated_basket_to_shop(basketId):
    basketInfo = db.execute_select_one_query("SELECT callbackURL, totalAmountWithDiscounts, shopId, consumerId FROM Basket WHERE id = {}".format(basketId))
    loyaltyId = db.execute_select_one_query("SELECT loyaltyId FROM ConsumerInShop WHERE shopId = {} AND consumerId = {}".format(basketInfo[2], basketInfo[3]))
    r = requests.patch(basketInfo[0], json=json.dumps({
        "consumerId": basketInfo[3],
        "loyaltyId": loyaltyId[0],
        "totalAmountWithDiscounts": basketInfo[1]
    }))

def user_exists(consumerId: int):
    return not db.execute_select_one_query("SELECT * FROM Consumer WHERE id = {}".format(consumerId)) is None

def basket_exists(basketId: int):
    return not db.execute_select_one_query("SELECT * FROM Basket WHERE id = {}".format(basketId)) is None

if __name__ == "__main__":
    app.run(debug=True, port=5002, host=REMOTE_HOST)