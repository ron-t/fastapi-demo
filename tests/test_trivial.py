from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_version():
    response = client.get("/")
    assert response.text == "v2024-05-08"
