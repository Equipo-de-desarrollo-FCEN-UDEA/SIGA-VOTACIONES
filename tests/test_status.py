from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session
from app.main import app
from app.config.database import get_session
from app.models.Status import Status  # Asegúrate de importar el modelo de datos

# Definir la URL de la base de datos en memoria para pruebas
TEST_DATABASE_URL = "sqlite:///test.sqlite?mode=rw"

# Crear el engine para la base de datos en memoria
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})

# Crear las tablas en la base de datos de prueba
SQLModel.metadata.create_all(engine)


def get_session_override():
    with Session(engine) as session:
        yield session

app.dependency_overrides[get_session] = get_session_override

client = TestClient(app)

def test_create_status():
    response = client.post(
        "/status/create",
        json={"name": "waiting"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "waiting"
    assert "id" in data

def test_get_all_status():
    client.post(
        "/status/create",
        json={"name": "waiting"},
    )
    
    response = client.get("/status/all")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_status():
    response = client.post(
        "/status/create",
        json={"name": "waiting"},
    )
    data = response.json()
    
    response = client.get(f"/status/{data['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "waiting"
    assert "id" in data