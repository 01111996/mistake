import requests
import pytest
BASE_URL = "https://postman-echo.com"

def test_get_no_params():
    response = requests.get(f"{BASE_URL}/get")
    assert response.status_code == 200, (
        f"Status 200, itog {response.status_code}"
    )
    data = response.json()
    assert data["args"] == {}, (
        f"Expectation args, itog: {data['args']}"
    )
    assert "postman-echo.com/get" in data["url"], (
        f"URL itog: {data['url']}"
    )   

def test_get_quarry_parameters():
    params = {
        "name": "Александр",
        "city": "Москва",
        "age": "18",
    }
    response = requests.get(f"{BASE_URL}/get", params=params)
    assert response.status_code == 200
    data = response.json()
    assert data["args"]["name"] == "Александр", (
        "Параметр 'name' не совпадает"
    )
    assert data["args"]["city"] == "Москва", (
        "Параметр 'city' не совпадает"
    )
    assert data["args"]["age"] == "18", (
        "Параметр 'age' не совпадает" 
    )

def test_post_json():
    payload = {
        "user": "Александр",
        "email": "alex@gmail.com",
        "admin": "admin",
        "online": True,
    }
    response = requests.post(f"{BASE_URL}/post", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["json"]["user"] == "Александр"
    assert data["json"]["email"] == "alex@gmail.com"
    assert data["json"]["admin"] == "admin"
    assert data["json"]["online"] is True
    assert "application/json" in data["headers"]["content-type"], (
        "application/json"
    )
def test_post_form():
    form_data = {
        "login": "login_1",
        "password": "12345670",
        "save": "on",
    }
    response = requests.post(f"{BASE_URL}/post", data=form_data)
    assert response.status_code == 200
    data = response.json()
    assert data["form"]["login"] == "login_1""
    assert data["form"]["password"] == "12345670"
    assert data["form"]["save"] == "on"
    assert "application/x-www-form-urlencoded" in data["headers"]["content-type"], (
        "Content: application/x-www-form-urlencoded"
    )

def test_get_user_headers():
    custom_headers = {
        "API-Version": "1",
        "Client-ID": "pytest",
        "Authorization": "For testing purposes",
    }
    response = requests.get(f"{BASE_URL}/get", headers=custom_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["headers"]["api-version"] == "1"
    assert data["headers"]["client-id"] == "pytest"
    assert data["headers"]["authorization"] == "For testing purposes"
    assert "host" in data["headers"] 
    assert "user-agent" in data["headers"]
