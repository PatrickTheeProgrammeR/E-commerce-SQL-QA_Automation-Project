from fastapi import FastAPI, HTTPException
import sqlite3
app = FastAPI()
from pathlib import Path

DATABASE = Path(__file__).resolve().parent.parent / "data" / "ecommerce.db"

@app.get("/users/{user_id}", status_code=200)
def get_user(user_id : int):
    with sqlite3.connect(DATABASE) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE id = ?",
            (user_id,)
        )

        user = cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"]
    }


@app.post("/users", status_code=201)
def create_user(user: dict):
    with sqlite3.connect(DATABASE) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user["name"], user["email"])
        )

        connection.commit()

        user_id = cursor.lastrowid

    return {
        "id": user_id,
        "name": user["name"],
        "email": user["email"]
    }


@app.put("/users/{user_id}", status_code=200)
def update_user(user_id : int, user: dict):
    with sqlite3.connect(DATABASE) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE users
            SET name = ?, email = ?
            WHERE id = ?
            """,
            (
                user["name"],
                user["email"],
                user_id
            )
        )

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        connection.commit()

    return {
        "id": user_id,
        "name": user["name"],
        "email": user["email"]
    }


@app.delete("/users/{user_id}", status_code=200)
def delete_user(user_id : int):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )

        connection.commit()

        deleted = cursor.rowcount

    return {"deleted": deleted}



@app.get("/products/{product_id}", status_code=200)
def get_product(product_id: int):
    with sqlite3.connect(DATABASE) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM products WHERE id = ?",
            (product_id,)
        )

        product = cursor.fetchone()

        if product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return {
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
        }


@app.post("/products", status_code=201)
def create_product(product: dict):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO products (name, price) VALUES (?, ?)",
            (product["name"], product["price"])
        )

        connection.commit()

    product_id = cursor.lastrowid

    return {
        "id": product_id,
        "name": product["name"],
        "price": product["price"]
    }


@app.get("/orders/{order_id}", status_code=200)
def get_order(order_id: int):
    with sqlite3.connect(DATABASE) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM orders WHERE id = ?",
            (order_id,)
        )

        order = cursor.fetchone()

        if order is None:
            raise HTTPException(
                status_code=404,
                detail="Order not found"
            )

        return {
            "id": order["id"],
            "user_id": order["user_id"],
            "total_amount": order["total_amount"]
        }


@app.post("/orders", status_code=201)
def create_order(order: dict):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO orders (user_id, total_amount) VALUES (?, ?)",
            (order["user_id"], order["total_amount"])
        )

        connection.commit()

        order_id = cursor.lastrowid

    return {
        "id": order_id,
        "user_id": order["user_id"],
        "total_amount": order["total_amount"]
    }


@app.post("/orders/{order_id}/items", status_code=201)
def create_order_item(order_id: int, order_item: dict):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO order_items (order_id, product_id, quantity)
            VALUES (?, ?, ?)
            """,
            (
                order_id,
                order_item["product_id"],
                order_item["quantity"]
            )
        )

        connection.commit()

        order_item_id = cursor.lastrowid

    return {
        "id": order_item_id,
        "order_id": order_id,
        "product_id": order_item["product_id"],
        "quantity": order_item["quantity"]
    }