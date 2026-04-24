from ecommerce.metrics import summarize_response_times


def test_desempenho_p95_produto_menor_500ms(client, benchmark):
    """Desempenho: tempo de resposta P95 deve ficar abaixo de 500ms."""

    response = benchmark(lambda: client.get("/produto/1"))
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_calculo_p95_aprova_meta_500ms():
    tempos_ms = [120, 130, 140, 150, 160, 170, 180, 190, 200, 450]
    resumo = summarize_response_times(tempos_ms)
    assert resumo["p95_ms"] < 500
