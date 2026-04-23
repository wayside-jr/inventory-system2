import pytest
from app import app
from unittest.mock import patch

@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client

def test_create_item(client):
    res = client.post("/items", json={
        "name": "Milk",
        "barcode": "123",
        "price": 10,
        "quantity": 5,
        "category": "dairy"
    })

    assert res.status_code == 201
    data = res.get_json()
    assert data["name"] == "Milk"

def test_get_items(client):
    res = client.get("/items")

    assert res.status_code == 200
    data = res.get_json()
    assert "items" in data


def test_get_single_item(client):
    client.post("/items", json={
        "name": "Bread",
        "barcode": "999",
        "price": 5,
        "quantity": 1,
        "category": "food"
    })

    res = client.get("/items/1")

    assert res.status_code == 200
    assert res.get_json()["name"] == "Bread"

def test_update_item(client):
    client.post("/items", json={
        "name": "Sugar",
        "barcode": "888",
        "price": 3,
        "quantity": 2,
        "category": "food"
    })

    res = client.patch("/items/1", json={
        "price": 20
    })

    assert res.status_code == 200

    updated = client.get("/items/1").get_json()
    assert updated["price"] == 20