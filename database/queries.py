import sqlite3


def get_product_by_name(name):
    with sqlite3.connect("ecommerce.db") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products WHERE name = ?", (name,))
        row = cursor.fetchone()

        if row is None:
            raise ValueError("Product not found")

        result = dict(row)
        return result




