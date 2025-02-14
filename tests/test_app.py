import pytest
import requests

BASE_URL = "http://localhost:8000"

def test_add():
    response = requests.get(f"{BASE_URL}/add?a=10&b=5")
    assert response.status_code == 200
    assert response.json()['result'] == 15

def test_subtract():
    response = requests.get(f"{BASE_URL}/subtract?a=10&b=5")
    assert response.status_code == 200
    assert response.json()['result'] == 5

def test_multiply():
    response = requests.get(f"{BASE_URL}/multiply?a=10&b=5")
    assert response.status_code == 200
    assert response.json()['result'] == 50

def test_divide():
    response = requests.get(f"{BASE_URL}/divide?a=10&b=5")
    assert response.status_code == 200
    assert response.json()['result'] == 2

def test_divide_by_zero():
    response = requests.get(f"{BASE_URL}/divide?a=10&b=0")
    assert response.status_code == 400
