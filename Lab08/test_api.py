import os

import jsonschema
import pytest
import requests

BASE_URL = os.getenv("BASE_URL", "https://reqres.in/api")
HEADERS = {"x-api-key": os.getenv("REQRES_API_KEY", "reqres-free-v1")}
TIMEOUT = 10

USER_RESOURCE_SCHEMA = {
    "type": "object",
    "required": ["data", "support"],
    "properties": {
        "data": {
            "type": "object",
            "required": ["id", "email", "first_name", "last_name", "avatar"],
            "properties": {
                "id": {"type": "integer"},
                "email": {"type": "string", "format": "email"},
                "first_name": {"type": "string", "minLength": 1},
                "last_name": {"type": "string", "minLength": 1},
                "avatar": {"type": "string", "minLength": 1},
            },
            "additionalProperties": True,
        },
        "support": {
            "type": "object",
            "required": ["url", "text"],
            "properties": {
                "url": {"type": "string", "minLength": 1},
                "text": {"type": "string"},
            },
            "additionalProperties": True,
        },
    },
    "additionalProperties": True,
}


@pytest.fixture
def usuario_criado():
    """Cria um usuário antes do teste e envia DELETE ao final como setup/teardown."""
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(
        f"{BASE_URL}/users", json=payload, headers=HEADERS, timeout=TIMEOUT
    )
    assert response.status_code == 201
    usuario = response.json()

    yield usuario

    user_id = usuario.get("id")
    if user_id is not None:
        requests.delete(f"{BASE_URL}/users/{user_id}", headers=HEADERS, timeout=TIMEOUT)



def test_listar_usuarios():
    """GET /users?page=2 deve retornar status 200 e uma lista não vazia."""
    response = requests.get(
        f"{BASE_URL}/users", params={"page": 2}, headers=HEADERS, timeout=TIMEOUT
    )

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0



def test_schema_usuario_existente():
    """GET /users/2 deve retornar status 200 e obedecer ao schema definido."""
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS, timeout=TIMEOUT)

    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=USER_RESOURCE_SCHEMA)



def test_usuario_inexistente():
    """GET /users/23 deve retornar 404 para um recurso inexistente."""
    response = requests.get(f"{BASE_URL}/users/23", headers=HEADERS, timeout=TIMEOUT)

    assert response.status_code == 404



def test_criar_usuario():
    """POST /users deve retornar 201 e incluir id no corpo da resposta."""
    payload = {"name": "joao", "job": "qa"}
    response = requests.post(
        f"{BASE_URL}/users", json=payload, headers=HEADERS, timeout=TIMEOUT
    )

    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]



def test_atualizar_usuario_com_patch():
    """PATCH /users/2 deve retornar 200 e refletir o campo alterado."""
    payload = {"job": "senior qa"}
    response = requests.patch(
        f"{BASE_URL}/users/2", json=payload, headers=HEADERS, timeout=TIMEOUT
    )

    assert response.status_code == 200
    data = response.json()
    assert data["job"] == payload["job"]
    assert "updatedAt" in data



def test_deletar_usuario():
    """DELETE /users/2 deve retornar status 204."""
    response = requests.delete(f"{BASE_URL}/users/2", headers=HEADERS, timeout=TIMEOUT)

    assert response.status_code == 204



def test_validacao_login_sem_senha():
    """POST /login sem senha deve retornar erro 4xx para dados inválidos."""
    payload = {"email": "eve.holt@reqres.in"}
    response = requests.post(
        f"{BASE_URL}/login", json=payload, headers=HEADERS, timeout=TIMEOUT
    )

    assert 400 <= response.status_code < 500
    data = response.json()
    assert "error" in data



def test_login_com_credencial_valida():
    """POST /login com credenciais válidas deve autenticar e retornar token."""
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(
        f"{BASE_URL}/login", json=payload, headers=HEADERS, timeout=TIMEOUT
    )

    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert isinstance(data["token"], str)
    assert len(data["token"]) > 0



def test_login_sem_credencial():
    """POST /login sem credenciais deve falhar com status 4xx e mensagem de erro."""
    response = requests.post(
        f"{BASE_URL}/login", json={}, headers=HEADERS, timeout=TIMEOUT
    )

    assert 400 <= response.status_code < 500
    data = response.json()
    assert "error" in data



def test_criar_com_fixture(usuario_criado):
    """Usa fixture para verificar que o recurso criado no setup possui id."""
    assert "id" in usuario_criado
    assert usuario_criado["name"] == "morpheus"
    assert usuario_criado["job"] == "leader"



def test_tempo_de_resposta():
    """GET /users/2 deve responder em menos de 2 segundos."""
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS, timeout=TIMEOUT)

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2.0
