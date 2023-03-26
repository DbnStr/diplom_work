from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route("/baskets", methods=['POST'])
def hello_world():
    data = json.JSONDecoder().decode(request.json)

    payment_link = "http://127.0.0.1:5002/baskets/" + str(data["id"])
    response_body = {"payment_link": payment_link}

    return Response(json.dumps(response_body), status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True, port=5002)