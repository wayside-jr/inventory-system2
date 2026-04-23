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

# get all items 
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({
        "count": len(items),
        "items": items
    }) 

# get one item 
@app.route("/items/<int:id>", methods=["GET"])
def get_item(id):
    item = next((i for i in items if i["id"] == id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item)

