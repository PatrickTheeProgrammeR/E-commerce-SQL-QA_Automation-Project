from database.queries import get_product_by_name
import pytest

def test_get_product_by_name():
    product = get_product_by_name("Keyboard")

    assert product["name"] == "Keyboard"


def test_get_product_by_name_not_found():
    with pytest.raises(ValueError):
        get_product_by_name("iPhone")