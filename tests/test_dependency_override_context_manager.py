from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


async def real_dependency():
    return {"source": "real"}


@app.get("/route/")
async def route(data: dict = Depends(real_dependency)):
    return data


async def fake_dependency():
    return {"source": "fake"}


client = TestClient(app)


def test_original_state_is_saved():
    app.dependency_overrides[real_dependency] = fake_dependency
    with app.override_dependencies({real_dependency: fake_dependency}):
        pass
    assert app.dependency_overrides == {real_dependency: fake_dependency}
    app.dependency_overrides = {}


def test_overrides_active_during_block():
    with app.override_dependencies({real_dependency: fake_dependency}):
        response = client.get("/route/")
    assert response.status_code == 200
    assert response.json() == {"source": "fake"}


def test_cleanup_after_block():
    with app.override_dependencies({real_dependency: fake_dependency}):
        pass
    assert app.dependency_overrides == {}
