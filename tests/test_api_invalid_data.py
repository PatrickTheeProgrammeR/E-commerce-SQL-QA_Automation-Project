import requests

BASE_URL = "http://localhost:8000"


def test_create_user_without_email():
    response = requests.post(
        f"{BASE_URL}/users",
        json = {
            "name": "Jan"
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Name and email are required"


def test_create_user_with_empty_name():
    response = requests.post(
        f"{BASE_URL}/users",
        json={
            "name": "",
            "email": "jan@example.com"
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Name must be a non-empty string"


def test_create_user_with_invalid_email():
    response = requests.post(
        f"{BASE_URL}/users",
        json={
            "name": "Jan",
            "email": "niepoprawny-email"
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Email is invalid"



