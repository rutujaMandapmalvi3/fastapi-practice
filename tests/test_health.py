from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)

disabled_app = FastAPI(health_url=None)
disabled_client = TestClient(disabled_app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200, response.text
    assert response.json() == {"status": "ok"}


def test_health_disabled():
    response = disabled_client.get("/health")
    assert response.status_code == 404
