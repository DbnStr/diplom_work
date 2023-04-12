from flask import Flask, request, Response
import json

app = Flask(__name__)

json_basket = None

@app.route("/baskets", methods=['POST'])
def post_new_basket():
    data = json.JSONDecoder().decode(request.json)
    json_basket = request.json

    payment_link = "http://127.0.0.1:5002/baskets/" + str(data["id"])
    response_body = {"payment_link": payment_link}

    return Response(json.dumps(response_body), status=200, mimetype='application/json')

@app.route("/baskets/<string:basket_id>", methods=['GET'])
def get_basket(basket_id):
    queries = request.args.to_dict()
    if queries.get('user_id'):
        return Response(json_basket, status=200, mimetype='application/json')
    else:
        print("No user_id in request")

if __name__ == "__main__":
    app.run(debug=True, port=5002)