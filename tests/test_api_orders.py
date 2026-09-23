import requests
import sqlite3
from pathlib import Path

DATABASE = Path(__file__).resolve().parent.parent / "data" / "ecommerce.db"
BASE_URL = "http://localhost:8000"


def test_get_order():
    response = requests.get(f"{BASE_URL}/orders/1")

    assert response.status_code == 200

    data = response.json()

    with sqlite3.connect(DATABASE) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM orders WHERE id = ?",
            (1,)
        )

    order = cursor.fetchone()

    assert order is not None
    assert data["id"] == order["id"]
    assert data["user_id"] == order["user_id"]
    assert data["total_amount"] == order["total_amount"]



def test_get_order_not_found():
    response = requests.get(f"{BASE_URL}/orders/999")

    assert response.status_code == 404



def test_create_order():
    response = requests.post(
        f"{BASE_URL}/orders",
        json={
            "user_id": 2,
            "total_amount": 599.99
        }
    )

    assert response.status_code == 201

    data = response.json()

    with sqlite3.connect(DATABASE) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM orders WHERE id = ?",
            (data["id"],)
        )

        order = cursor.fetchone()

        assert order is not None
        assert data["id"] == order["id"]
        assert data["user_id"] == order["user_id"]
        assert data["total_amount"] == order["total_amount"]

        cursor.execute(
            "DELETE FROM orders WHERE id = ?",
            (data["id"],)
        )

        connection.commit()



def test_create_order_item():
    order_response = requests.post(
        f"{BASE_URL}/orders",
        json={
            "user_id": 2,
            "total_amount": 199.98
        }
    )

    assert order_response.status_code == 201

    order_id = order_response.json()["id"]

    response = requests.post(
        f"{BASE_URL}/orders/{order_id}/items",
        json={
            "product_id": 2,
            "quantity": 2
        }
    )

    assert response.status_code == 201

    data = response.json()

    with sqlite3.connect(DATABASE) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM order_items WHERE id = ?",
            (data["id"],)
        )

        order_item = cursor.fetchone()


        assert order_item is not None
        assert data["id"] == order_item["id"]
        assert data["order_id"] == order_item["order_id"]
        assert data["product_id"] == order_item["product_id"]
        assert data["quantity"] == order_item["quantity"]

        cursor.execute(
            "DELETE FROM order_items WHERE id = ?",
            (data["id"],)
        )

        cursor.execute(
            "DELETE FROM orders WHERE id = ?",
            (order_id,)
        )

        connection.commit()
