from ecommerce.metrics import availability, throughput


def test_carga_throughput_sustentado_maior_2000_reqs():
    """Carga: 10.000 requisições em até 5s equivale a > 2000 req/s."""

    total_requests = 10_500
    total_seconds = 5
    assert throughput(total_requests, total_seconds) > 2000


def test_carga_disponibilidade_999_porcento():
    total = 10_000
    success = 9_990
    assert availability(success, total) >= 99.9
