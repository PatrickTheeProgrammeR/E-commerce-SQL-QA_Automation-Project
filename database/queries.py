import sqlite3
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.models import Product

DATABASE = Path(__file__).resolve().parent.parent / "data" / "ecommerce.db"


def get_product_by_name(name):
    with sqlite3.connect(DATABASE) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products WHERE name = ?", (name,))
        row = cursor.fetchone()

        if row is None:
            raise ValueError("Product not found")

        result = dict(row)
        return result


engine = create_engine(f"sqlite:///{DATABASE}")

def get_product_by_name_orm(name):
    with Session(engine) as session:
        stmt = select(Product).where(Product.name == name)
        product = session.scalars(stmt).first()
        return product


def create_product(name, price):
    with Session(engine) as session:
        product = Product(name=name, price=price)
        session.add(product)
        session.commit()
        session.refresh(product)
        return product


def update_product_price(product_id, new_price):
    with Session(engine) as session:
        product = session.get(Product, product_id)

        if product is None:
            raise ValueError("Product not found")

        product.price = new_price
        session.commit()
        session.refresh(product)

        return product


def delete_product(product_id):
    with Session(engine) as session:
        product = session.get(Product, product_id)

        if product is None:
            raise ValueError("Product not found")

        session.delete(product)
        session.commit()
