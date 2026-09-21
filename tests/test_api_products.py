import requests
import sqlite3
from pathlib import Path

DATABASE = Path(__file__).resolve().parent.parent / "data" / "ecommerce.db"


def test_get_product():
    url = "http://localhost:8000/products/1"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()

    with sqlite3.connect(DATABASE) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM products WHERE id = ?",
            (1,)
        )

        product = cursor.fetchone()

    assert product is not None
    assert data["id"] == product["id"]
    assert product["name"] == product["name"]
    assert product["price"] == product["price"]


def test_get_product_not_found():
    url = "http://localhost:8000/products/999"
    response = requests.get(url)

    assert response.status_code == 404


