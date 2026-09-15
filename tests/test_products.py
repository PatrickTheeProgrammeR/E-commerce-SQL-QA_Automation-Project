from database.queries import get_product_by_name, get_product_by_name_orm
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