from itertools import product
from database.models import Product
from database.queries import get_product_by_name, get_product_by_name_orm, create_product, update_product_price, delete_product
import pytest

def test_get_product_by_name():
    product = get_product_by_name("Keyboard")

    assert product["name"] == "Keyboard"


def test_get_product_by_name_not_found():
    with pytest.raises(ValueError):
        get_product_by_name("iPhone")


def test_get_product_by_name_orm():
    product_orm = get_product_by_name_orm("Keyboard")

    assert product_orm.name == "Keyboard"


def test_create_product():
    product_create = create_product("Monitor", 899.99)

    assert product_create.name == "Monitor"
    assert product_create.price == 899.99


def test_update_product_price():
    product_id = get_product_by_name_orm("Keyboard").id
    product_update = update_product_price(product_id, 279.99)

    assert product_update.price == 279.99


def test_delete_product():
    product_id = get_product_by_name_orm("Monitor").id
    delete_product(product_id)

    assert get_product_by_name_orm("Monitor") is None