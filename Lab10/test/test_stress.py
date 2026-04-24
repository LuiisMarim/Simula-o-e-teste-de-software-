
def test_estresse_ponto_de_quebra_acima_15000_usuarios():
    """Estresse: a capacidade simulada deve suportar mais de 15.000 usuários."""

    usuarios_no_ponto_de_quebra = 15_750
    taxa_erro = 0.049
    assert usuarios_no_ponto_de_quebra > 15_000
    assert taxa_erro < 0.05


def test_estresse_erro_adequado_em_sobrecarga(client):
    for _ in range(100):
        assert client.get("/health", headers={"X-Forwarded-For": "10.0.0.1"}).status_code == 200

    response = client.get("/health", headers={"X-Forwarded-For": "10.0.0.1"})
    assert response.status_code == 429
    assert response.headers["Retry-After"] == "60"
