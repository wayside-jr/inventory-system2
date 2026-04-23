from flask import Flask, request, jsonify

app = Flask(__name__)


items = []

# create item 

@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()

    new_item = {
        "id": len(items) + 1,
        "name": data["name"],
        "barcode": data.get("barcode"),
        "price": data.get("price"),
        "quantity": data.get("quantity"),
        "category": data.get("category")
    }

    items.append(new_item)

    return jsonify(new_item), 201

