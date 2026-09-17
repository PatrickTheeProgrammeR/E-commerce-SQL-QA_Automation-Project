from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

@app.get("/users/{user_id}", status_code=200)
def get_user(user_id : int):
    with sqlite3.connect("ecommerce.db") as connection:
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
    with sqlite3.connect("ecommerce.db") as connection:
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
def update_user(user_id : int, user : dict):
    with sqlite3.connect("ecommerce.db") as connection:
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

        connection.commit()

    return {
        "id": user_id,
        "name": user["name"],
        "email": user["email"]
    }


@app.delete("/users/{user_id}", status_code=200)
def delete_user(user_id : int):
    with sqlite3.connect("ecommerce.db") as connection:
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )

        connection.commit()

        deleted = cursor.rowcount

    return {"deleted": deleted}