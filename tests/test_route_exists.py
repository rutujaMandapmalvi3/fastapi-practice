from fastapi import FastAPI

app = FastAPI()


@app.get("/items", name="list_items")
def list_items():
    return []


def test_route_exists_returns_true_for_existing_route():
    assert app.route_exists("list_items") is True


def test_route_exists_returns_false_for_missing_route():
    assert app.route_exists("nonexistent") is False
