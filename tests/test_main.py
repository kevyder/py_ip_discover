from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_ip_info():
    response = client.get("/ip/45.238.183.189")
    assert response.status_code == 200
