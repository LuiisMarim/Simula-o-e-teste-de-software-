import pytest
import sys
sys.path.insert(0, '/workspaces/Simula-o-e-teste-de-software-/Lab03/src')

from hypothesis import given, strategies as st
from frete import calcular_frete

class TestSistemaFrete:

    @pytest.mark.parametrize("peso, destino, valor, esperado", [
        (0.5, "mesma regiao", 100.0, 10.0),
        (3.0, "outra regiao", 150.0, 22.5),
        (15.0, "internacional", 50.0, 50.0),
        (2.0, "mesma regiao", 250.0, 0.0),
        (10.0, "outra regiao", 300.0, 0.0)
    ])
    def test_classes_equivalencia(self, peso, destino, valor, esperado):
        assert calcular_frete(peso, destino, valor) == esperado

    @pytest.mark.parametrize("peso, esperado", [
        (0.9, 10.0), (1.0, 10.0), (1.1, 15.0),
        (4.9, 15.0), (5.0, 15.0), (5.1, 25.0),
        (19.9, 25.0), (20.0, 25.0)
    ])
    def test_valores_limite_peso(self, peso, esperado):
        assert calcular_frete(peso, "mesma regiao", 100.0) == esperado

    def test_valor_limite_excecao(self):
        with pytest.raises(ValueError):
            calcular_frete(20.1, "mesma regiao", 100.0)

    @pytest.mark.parametrize("peso, destino, valor, falha", [
        (25.0, "mesma regiao", 100.0, True),
        (10.0, "marte", 100.0, True),
        (10.0, "internacional", 250.0, False),
        (3.0, "mesma regiao", 100.0, False),
        (3.0, "outra regiao", 100.0, False),
        (3.0, "internacional", 100.0, False)
    ])
    def test_tabela_decisao(self, peso, destino, valor, falha):
        if falha:
            with pytest.raises(ValueError):
                calcular_frete(peso, destino, valor)
        else:
            resultado = calcular_frete(peso, destino, valor)
            assert resultado >= 0.0

    @pytest.mark.parametrize("peso, destino", [
        (0.0, "mesma regiao"),
        (-5.0, "outra regiao")
    ])
    def test_entradas_invalidas_peso(self, peso, destino):
        with pytest.raises(ValueError):
            calcular_frete(peso, destino, 100.0)

    @given(
        st.floats(min_value=0.1, max_value=20.0),
        st.sampled_from(["mesma regiao", "outra regiao", "internacional"]),
        st.floats(min_value=0.0, max_value=200.0)
    )
    def test_propriedade_frete_nunca_negativo(self, peso, destino, valor):
        assert calcular_frete(peso, destino, valor) >= 0.0

    @given(
        st.floats(min_value=0.1, max_value=20.0),
        st.sampled_from(["mesma regiao", "outra regiao", "internacional"]),
        st.floats(min_value=200.01, max_value=10000.0)
    )
    def test_propriedade_pedido_caro_frete_gratis(self, peso, destino, valor):
        assert calcular_frete(peso, destino, valor) == 0.0

    @given(
        st.floats(min_value=0.1, max_value=20.0),
        st.floats(min_value=0.0, max_value=200.0)
    )
    def test_propriedade_frete_outra_regiao_maior(self, peso, valor):
        frete_mesma = calcular_frete(peso, "mesma regiao", valor)
        frete_outra = calcular_frete(peso, "outra regiao", valor)
        assert frete_outra > frete_mesma