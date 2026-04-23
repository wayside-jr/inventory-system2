from flask import Flask, request, jsonify
import requests

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

# update item
@app.route("/items/<int:id>", methods=["PATCH"])
def update_item(id):
    item = next((i for i in items if i["id"] == id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()

    item["name"] = data.get("name", item["name"])
    item["barcode"] = data.get("barcode", item["barcode"])
    item["price"] = data.get("price", item["price"])
    item["quantity"] = data.get("quantity", item["quantity"])
    item["category"] = data.get("category", item["category"])

    return jsonify({
        "message": "Item updated",
        "item": item
    })

# Delete item

@app.route("/items/<int:id>", methods=["DELETE"])
def delete_item(id):
    global items

    item = next((i for i in items if i["id"] == id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    items = [i for i in items if i["id"] != id]

    return jsonify({"message": "Item deleted"})


# external api
#get products
@app.route("/api/products/<string:name>", methods=["GET"])
def get_products(name):

    url = f"https://world.openfoodfacts.org/cgi/search.pl"

    params = {
        "search_terms": name,
        "search_simple": 1,
        "action": "process",
        "json": 1
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, params=params, headers=headers, timeout=10)

    try:
        data = res.json()
    except Exception:
        return {
            "error": "External API returned invalid response",
            "status_code": res.status_code
        }, 500

    products = []

    for p in data.get("products", []):
        if not p:
            continue

        products.append({
            "name": p.get("product_name"),
            "brand": p.get("brands"),
            "barcode": p.get("code")
        })

    return {
        "count": len(products),
        "products": products
    }
if __name__ == "__main__":
    app.run(debug=True)