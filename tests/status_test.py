import os
import pytest
from httpx import ASGITransport, AsyncClient
from sqlmodel import SQLModel, Session

from sqlalchemy.ext.asyncio import create_async_engine

from app.config.database import get_engine, get_sesion
from app.main import app
from app.models.Status import StatusReadWithVotings


url_status = "http://localhost:8002/status"
test_engine = get_engine("sqlite:///test.sqlite")
SQLModel.metadata.create_all(test_engine)

@pytest.fixture(autouse=True)
async def database():
    yield test_engine
    await test_engine.dispose()  # Asegurarse de cerrar cualquier conexión
    await os.remove("test.sqlite")  # Eliminar el archivo físico
    test_engine = await get_engine("sqlite:///test.sqlite?mode=rw")
    await SQLModel.metadata.create_all(test_engine)

def override_get_sesion():
    with Session(test_engine) as session:
        yield session
        session.close()

app.dependency_overrides[get_sesion] = override_get_sesion


@pytest.mark.asyncio
async def test_get_status():
    async with AsyncClient(transport=ASGITransport(app=app), base_url=url_status) as ac:
        # Crear un nuevo estado
        post_response = await ac.post("/create", json={"id": "test1", "name": "waiting"})
        assert post_response.status_code == 201 # Verificar que la creación fue exitosa

        # Obtener el estado creado
        response = await ac.get("/test1")
        assert response.status_code == 200
        # Aquí se podría reactivar la verificación del tipo si es necesario
        # assert isinstance(StatusReadWithVotings(**response.json()), StatusReadWithVotings)

@pytest.mark.asyncio
async def test_get_all_status():
    async with AsyncClient(transport=ASGITransport(app=app), base_url=url_status) as ac:
        response = await ac.get("/all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_status():
    async with AsyncClient(transport=ASGITransport(app=app), base_url=url_status) as ac:
        response = await ac.post("/create", 
                                 json={"name": "waiting"})
    assert response.status_code == 201





# Limpia las dependencias sobrescritas después de las pruebas
@pytest.fixture(autouse=True)
def cleanup():
    yield
    app.dependency_overrides.clear()

"""
@pytest.mark.asyncio
async def test_create_item():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/items/", json={"id": 1, "name": "Test Item"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test Item"}

@pytest.mark.asyncio
async def test_read_item():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.post("/items/", json={"id": 1, "name": "Test Item"})
        response = await ac.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test Item"}

@pytest.mark.asyncio
async def test_read_item_not_found():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
"""