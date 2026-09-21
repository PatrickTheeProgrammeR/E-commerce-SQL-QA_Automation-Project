import pytest
from sqlalchemy.orm import Session

from database.models import OrderItem
from database.queries import engine, get_order_by_id, create_order, add_order_item

def test_get_order_by_id():
    order = get_order_by_id(1)

    assert order.id == 1
    assert order.user_id == 2
    assert order.total_amount == 249.99


def test_get_order_by_id_not_found():
    with pytest.raises(ValueError):
        get_order_by_id(999)


def test_create_order():
    order = create_order(1, 199.99)

    assert order.user_id == 1
    assert order.total_amount == 199.99

    with Session(engine) as session:
        session.delete(order)
        session.commit()


def test_add_order_item():
    order_item = add_order_item(1, 1, 2)

    assert order_item.order_id == 1
    assert order_item.product_id == 1
    assert order_item.quantity == 2

    with Session(engine) as session:
        saved_order_item = session.get(OrderItem, order_item.id)
        session.delete(saved_order_item)
        session.commit()
