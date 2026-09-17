import sqlite3
import pytest
from pathlib import Path

DATABASE = Path(__file__).resolve().parent.parent / "data" / "ecommerce.db"


@pytest.fixture(autouse=True)
def reset_user():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM users WHERE id = 1")

        cursor.execute(
            """
            INSERT INTO users (id, name, email)
            VALUES (1, 'Adam', 'adam@example.com')
            """
        )

        connection.commit()