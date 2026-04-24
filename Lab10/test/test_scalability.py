from ecommerce.metrics import horizontal_efficiency


def test_escalabilidade_eficiencia_horizontal_maior_80_porcento():
    """Escalabilidade: 4 nós devem manter eficiência horizontal > 80%."""

    baseline_1_no = 600
    throughput_4_nos = 2050
    eficiencia = horizontal_efficiency(throughput_4_nos, baseline_1_no, nodes=4)
    assert eficiencia > 80
