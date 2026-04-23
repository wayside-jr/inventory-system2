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