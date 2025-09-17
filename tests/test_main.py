# tests/test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_positive_numbers():
    """Test adding two positive numbers."""
    response = client.get("/add?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_subtract_positive_numbers():
    """Test subtracting two positive numbers. ..."""
    response = client.get("/subtract?a=10&b=4")
    assert response.status_code == 200
    assert response.json() == {"result": 6}