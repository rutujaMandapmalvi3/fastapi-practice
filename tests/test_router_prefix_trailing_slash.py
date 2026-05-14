import pytest
from fastapi import APIRouter, FastAPI
from fastapi.testclient import TestClient


def test_prefix_trailing_slash_raises():
    with pytest.raises(
        ValueError,
        match="A path prefix must not end with '/', as the routes will start with '/'",
    ):
        APIRouter(prefix="/items/")


def test_prefix_valid_returns_200():
    router = APIRouter(prefix="/items")

    @router.get("/all")
    def get_items():
        return ["item1", "item2"]

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)

    response = client.get("/items/all")
    assert response.status_code == 200, response.text
