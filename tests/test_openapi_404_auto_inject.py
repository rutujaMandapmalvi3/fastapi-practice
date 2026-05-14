from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"id": item_id}


@app.get("/custom-404", responses={404: {"description": "Custom not found"}})
def custom_404_route():
    return {"ok": True}


client = TestClient(app)


def test_404_auto_injected_in_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    responses = schema["paths"]["/items/{item_id}"]["get"]["responses"]
    assert "404" in responses
    assert responses["404"]["description"] == "Not Found"


def test_404_schema_in_components():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    assert "HTTPError" in schema["components"]["schemas"]
    assert schema["components"]["schemas"]["HTTPError"]["properties"]["detail"]["type"] == "string"


def test_explicit_404_not_overwritten():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    responses = schema["paths"]["/custom-404"]["get"]["responses"]
    assert responses["404"]["description"] == "Custom not found"
