import click
import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def print_response(res):
    try:
        data = res.json()
        click.echo(json.dumps(data, indent=2))
    except:
        click.echo(res.text)


@click.command()
def list_items():
    """Get all items"""
    res = requests.get(f"{BASE_URL}/items")
    print_response(res)

@click.command()
@click.option("--name", required=True)
@click.option("--barcode")
@click.option("--price", type=float)
@click.option("--quantity", type=int)
@click.option("--category")
def create(name, barcode, price, quantity, category):

    data = {
        "name": name,
        "barcode": barcode,
        "price": price,
        "quantity": quantity,
        "category": category
    }

    res = requests.post(f"{BASE_URL}/items", json=data)
    print_response(res)

@click.command()
@click.argument("item_id")
def get(item_id):
    res = requests.get(f"{BASE_URL}/items/{item_id}")
    print_response(res)

@click.command()
@click.argument("item_id")
@click.option("--name")
@click.option("--barcode")
@click.option("--price", type=float)
@click.option("--quantity", type=int)
@click.option("--category")
def update(item_id, name, barcode, price, quantity, category):

    data = {}

    if name:
        data["name"] = name
    if barcode:
        data["barcode"] = barcode
    if price is not None:
        data["price"] = price
    if quantity is not None:
        data["quantity"] = quantity
    if category:
        data["category"] = category

    res = requests.patch(f"{BASE_URL}/items/{item_id}", json=data)
    print_response(res)
    

@click.command()
@click.argument("item_id")
def delete(item_id):
    res = requests.delete(f"{BASE_URL}/items/{item_id}")
    print_response(res)

@click.group()
def cli():
    pass


cli.add_command(list_items)
cli.add_command(create)
cli.add_command(get)
cli.add_command(update)
cli.add_command(delete)

if __name__ == "__main__":
    cli()