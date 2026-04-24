
def test_seguranca_rate_limiting_100_req_min_ip(client):
    for _ in range(100):
        response = client.get("/produto/1", headers={"X-Forwarded-For": "192.168.1.10"})
        assert response.status_code == 200

    blocked = client.get("/produto/1", headers={"X-Forwarded-For": "192.168.1.10"})
    assert blocked.status_code == 429


def test_seguranca_sql_injection_rejeitada(client):
    response = client.get("/buscar", params={"q": "' OR '1'='1"})
    assert response.status_code == 400


def test_seguranca_xss_sanitizado(client):
    response = client.get("/buscar", params={"q": "<img src=x>"})
    assert response.status_code == 200
    assert response.json()["query"] == "&lt;img src=x&gt;"


def test_seguranca_admin_sem_token_401(client):
    response = client.get("/admin")
    assert response.status_code == 401
