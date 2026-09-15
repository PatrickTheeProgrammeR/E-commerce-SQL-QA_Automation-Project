import sqlite3
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.models import Product


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


engine = create_engine("sqlite:///ecommerce.db")

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


