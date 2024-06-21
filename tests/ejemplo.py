import pytest
from httpx import ASGITransport, AsyncClient
from sqlmodel import SQLModel, Session
from app.config.database import get_sesion, get_engine
from app.main import app

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

test_engine = get_engine(DATABASE_URL, echo=True)
SQLModel.metadata.create_all(test_engine)

async def override_get_sesion():
    async with Session(test_engine) as session:
        yield session
        session.close()

async def override_get_sesion():
    async with TestSessionLocal() as session:
        yield session

app.dependency_overrides[get_sesion] = override_get_sesion

@pytest.fixture(scope="module", autouse=True)
async def prepare_database():
    async with test_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    print("Database setup complete")
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

@pytest.mark.asyncio
async def test_get_status(prepare_database):
    print("Starting test_get_status")
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost:8002/status") as ac:
        post_response = await ac.post("/create", json={"id": "test1", "name": "waiting"})
        print("Post response status code:", post_response.status_code)
        assert post_response.status_code == 201
        response = await ac.get("/test1")
        print("Get response status code:", response.status_code)
        assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_all_status(prepare_database):
    print("Starting test_get_all_status")
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost:8002/status") as ac:
        response = await ac.get("/all")
    print("Get all response status code:", response.status_code)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_status(prepare_database):
    print("Starting test_create_status")
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost:8002/status") as ac:
        response = await ac.post("/create", json={"name": "waiting"})
    print("Create response status code:", response.status_code)
    assert response.status_code == 201

@pytest.fixture(autouse=True)
def cleanup():
    yield
    app.dependency_overrides.clear()
