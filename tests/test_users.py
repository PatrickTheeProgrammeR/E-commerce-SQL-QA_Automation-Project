import requests
import sqlite3


def test_get_user():
    with sqlite3.connect("ecommerce.db") as connection:
        connection.row_factory = sqlite3.Row
        url = "http://localhost:8000/users/1"
        response = requests.get(url)

        assert response.status_code == 200

        data = response.json()

        cursor = connection.cursor()
        cursor.execute(
            """SELECT * FROM users WHERE id = ?""",
            (1,)
        )

        user = cursor.fetchone()
        assert user is not None
        assert user["id"] == data["id"]
        assert user["name"] == data["name"]
        assert user["email"] == data["email"]



def test_create_user():
    with sqlite3.connect("ecommerce.db") as connection:
        connection.row_factory = sqlite3.Row
        url = "http://localhost:8000/users"
        response = requests.post(
            url,
            json={
                "name": "Jan Kowalski",
                "email": "jan@example.com"
            }
        )
        assert response.status_code == 201

        data = response.json()

        cursor = connection.cursor()
        cursor.execute(
            """SELECT * FROM users WHERE id = ?""", (data["id"],)
        )

        user = cursor.fetchone()
        assert user is not None
        assert user["id"] == data["id"]
        assert user["name"] == data["name"]
        assert user["email"] == data["email"]



def test_update_user():
    with sqlite3.connect("ecommerce.db") as connection:
        connection.row_factory = sqlite3.Row
        url = "http://localhost:8000/users/1"
        response = requests.put(
            url,
            json={
                "name": "Adam Nowak",
                "email": "adamnk@example.com"
            }
        )

        assert response.status_code == 200

        data = response.json()

        cursor = connection.cursor()
        cursor.execute(
            """SELECT * FROM users WHERE id = ?""",
            (1,)
        )

        user = cursor.fetchone()
        assert user is not None
        assert user["id"] == data["id"]
        assert user["name"] == data["name"]
        assert user["email"] == data["email"]



def test_delete_user():
    with sqlite3.connect("ecommerce.db") as connection:
        url = "http://localhost:8000/users/1"
        response = requests.delete(
            url,
        )

        assert response.status_code == 200

        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE id = ?",
            (1,)
        )

        user = cursor.fetchone()

        assert user is None