import sqlite3
from pathlib import Path

DATABASE = Path(__file__).resolve().parent / "ecommerce.db"

if DATABASE.exists():
    DATABASE.unlink()

with sqlite3.connect(DATABASE) as connection:
    cursor = connection.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            );
        """)

    connection.commit()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL
            );
        """)

    connection.commit()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                total_amount REAL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        """)

    connection.commit()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_items (
                id INTEGER PRIMARY KEY,
                order_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                FOREIGN KEY (order_id) REFERENCES orders(id),
                FOREIGN KEY (product_id) REFERENCES products(id)       
            );
        """)

    connection.commit()

    cursor.execute("""
            INSERT INTO users (name, email)
            VALUES
                ("Adam", "adam@example.com"),
                ("Ala", "ala@example.com"),
                ("Borys", "borys@example.com");      
        """)

    connection.commit()

    cursor.execute("""
            INSERT INTO products (name, price)
            VALUES
                ("Laptop", 3499.99),
                ("Mouse", 99.99),
                ("Keyboard", 249.99),
                ("Headphones", 399.99);      
        """)

    connection.commit()

    cursor.execute("""
            INSERT INTO orders (user_id, total_amount)
            VALUES
                (2, 249.99),
                (3, 399.99),
                (1, 3499.99),
                (2, 399.99);     
        """)

    connection.commit()

    cursor.execute("""
            INSERT INTO order_items (order_id, product_id, quantity)
            VALUES
                (1, 3, 1),
                (2, 4, 1),
                (3, 1, 1),
                (4, 4, 1);     
        """)

    connection.commit()

    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())



