"""
Parte 1 — Testes de Unidade
Testa cada método da Calculadora de forma isolada usando stub (MagicMock)
para o HistoricoRepositorio.
"""
import sys
from unittest.mock import MagicMock

import pytest

from src.calculadora import Calculadora


# ============================================================
# Fixture: cria calculadora com repositório stub para cada teste
# ============================================================
@pytest.fixture
def calc():
    repo = MagicMock()
    return Calculadora(repo)


# ============================================================
# 2.1 — Testes de Entrada e Saída
# ============================================================
class TestEntradaSaida:
    """Valida valores retornados e atualização do último resultado."""

    # --- somar ---
    def test_soma_retorna_valor_correto(self, calc):
        assert calc.somar(5, 3) == 8

    def test_soma_atualiza_ultimo_resultado(self, calc):
        calc.somar(5, 3)
        assert calc.obter_ultimo_resultado() == 8

    def test_soma_negativos(self, calc):
        assert calc.somar(-2, -3) == -5

    # --- subtrair ---
    def test_subtrair_retorna_valor_correto(self, calc):
        assert calc.subtrair(10, 4) == 6

    def test_subtrair_atualiza_ultimo_resultado(self, calc):
        calc.subtrair(10, 4)
        assert calc.obter_ultimo_resultado() == 6

    def test_subtrair_resultado_negativo(self, calc):
        assert calc.subtrair(3, 7) == -4

    # --- multiplicar ---
    def test_multiplicar_retorna_valor_correto(self, calc):
        assert calc.multiplicar(4, 5) == 20

    def test_multiplicar_atualiza_ultimo_resultado(self, calc):
        calc.multiplicar(4, 5)
        assert calc.obter_ultimo_resultado() == 20

    def test_multiplicar_por_zero(self, calc):
        assert calc.multiplicar(99, 0) == 0

    # --- dividir ---
    def test_dividir_retorna_valor_correto(self, calc):
        assert calc.dividir(10, 2) == 5.0

    def test_dividir_atualiza_ultimo_resultado(self, calc):
        calc.dividir(10, 2)
        assert calc.obter_ultimo_resultado() == 5.0

    def test_dividir_resultado_fracionario(self, calc):
        assert calc.dividir(7, 2) == 3.5

    # --- potencia ---
    def test_potencia_retorna_valor_correto(self, calc):
        assert calc.potencia(2, 3) == 8

    def test_potencia_atualiza_ultimo_resultado(self, calc):
        calc.potencia(2, 3)
        assert calc.obter_ultimo_resultado() == 8

    def test_potencia_expoente_zero(self, calc):
        assert calc.potencia(5, 0) == 1


# ============================================================
# 2.2 — Testes de Tipagem
# ============================================================
class TestTipagem:
    """Confirma que tipos incorretos são rejeitados com TypeError."""

    # --- somar ---
    def test_soma_string_rejeitada(self, calc):
        with pytest.raises(TypeError):
            calc.somar("5", 3)

    def test_soma_none_rejeitado(self, calc):
        with pytest.raises(TypeError):
            calc.somar(None, 3)

    # --- subtrair ---
    def test_subtrair_string_rejeitada(self, calc):
        with pytest.raises(TypeError):
            calc.subtrair("a", 1)

    def test_subtrair_lista_rejeitada(self, calc):
        with pytest.raises(TypeError):
            calc.subtrair([1], 2)

    # --- multiplicar ---
    def test_multiplicar_string_rejeitada(self, calc):
        with pytest.raises(TypeError):
            calc.multiplicar(2, "3")

    def test_multiplicar_dict_rejeitado(self, calc):
        with pytest.raises(TypeError):
            calc.multiplicar({}, 1)

    # --- dividir ---
    def test_dividir_none_rejeitado(self, calc):
        with pytest.raises(TypeError):
            calc.dividir(10, None)

    def test_dividir_string_rejeitada(self, calc):
        with pytest.raises(TypeError):
            calc.dividir("10", 2)

    # --- potencia ---
    def test_potencia_string_rejeitada(self, calc):
        with pytest.raises(TypeError):
            calc.potencia("2", 3)

    def test_potencia_none_rejeitado(self, calc):
        with pytest.raises(TypeError):
            calc.potencia(2, None)

    # --- bool como subclasse de int ---
    def test_bool_aceito_na_soma(self, calc):
        """Em Python, bool é subclasse de int. isinstance(True, int) == True.
        Portanto True/False são aceitos como números. O comportamento é
        esperado: True == 1, False == 0."""
        resultado = calc.somar(True, False)
        assert resultado == 1  # True(1) + False(0) = 1

    def test_bool_aceito_na_multiplicacao(self, calc):
        resultado = calc.multiplicar(True, 5)
        assert resultado == 5  # True(1) * 5 = 5


# ============================================================
# 2.3 — Testes de Limite Inferior e Superior
# ============================================================
class TestLimites:
    """Verifica comportamento nas fronteiras do domínio numérico."""

    def test_limite_zero_soma(self, calc):
        assert calc.somar(0, 5) == 5

    def test_limite_float_pequeno_multiplicar(self, calc):
        assert calc.multiplicar(-1e-10, 2) == pytest.approx(-2e-10)

    def test_limite_float_grande_soma(self, calc):
        grande = sys.float_info.max / 2
        resultado = calc.somar(grande, grande)
        assert resultado != float("inf")  # não deve transbordar

    # --- dividir: divisor muito pequeno ---
    def test_dividir_divisor_muito_pequeno(self, calc):
        resultado = calc.dividir(1, 1e-300)
        assert resultado == pytest.approx(1e300)

    def test_dividir_divisor_proximo_de_zero(self, calc):
        resultado = calc.dividir(1.0, 1e-15)
        assert resultado == pytest.approx(1e15)

    # --- potencia: expoente negativo e fracionário ---
    def test_potencia_expoente_negativo(self, calc):
        assert calc.potencia(2, -1) == pytest.approx(0.5)

    def test_potencia_expoente_fracionario(self, calc):
        assert calc.potencia(9, 0.5) == pytest.approx(3.0)

    def test_potencia_base_negativa_expoente_par(self, calc):
        assert calc.potencia(-3, 2) == 9

    def test_soma_numeros_negativos_grandes(self, calc):
        grande = -sys.float_info.max / 2
        resultado = calc.somar(grande, grande)
        assert resultado != float("-inf")


# ============================================================
# 2.4 — Testes de Valores Fora do Intervalo
# ============================================================
class TestValoresForaDoIntervalo:
    """Verifica exceções para valores inválidos no domínio."""

    def test_divisao_por_zero_levanta_excecao(self, calc):
        with pytest.raises(ValueError):
            calc.dividir(10, 0)

    def test_divisao_zero_por_zero(self, calc):
        with pytest.raises(ValueError):
            calc.dividir(0, 0)


# ============================================================
# 2.5 — Testes de Mensagens de Erro
# ============================================================
class TestMensagensDeErro:
    """Verifica se as mensagens de erro correspondem ao contrato."""

    def test_mensagem_divisao_por_zero(self, calc):
        with pytest.raises(ValueError, match="Divisao por zero"):
            calc.dividir(5, 0)

    def test_mensagem_tipo_invalido_soma(self, calc):
        with pytest.raises(TypeError, match="Argumentos devem ser numeros"):
            calc.somar("x", 1)

    def test_mensagem_tipo_invalido_subtrair(self, calc):
        with pytest.raises(TypeError, match="Argumentos devem ser numeros"):
            calc.subtrair(1, "y")

    def test_mensagem_tipo_invalido_multiplicar(self, calc):
        with pytest.raises(TypeError, match="Argumentos devem ser numeros"):
            calc.multiplicar(None, 2)

    def test_mensagem_tipo_invalido_dividir(self, calc):
        with pytest.raises(TypeError, match="Argumentos devem ser numeros"):
            calc.dividir([], 1)

    def test_mensagem_tipo_invalido_potencia(self, calc):
        with pytest.raises(TypeError, match="Argumentos devem ser numeros"):
            calc.potencia("a", "b")


# ============================================================
# 2.6 — Testes de Fluxos de Controle
# ============================================================
class TestFluxosDeControle:
    """Exercita todos os caminhos (if/else) de cada método."""

    # somar — caminho normal
    def test_caminho_soma_normal(self, calc):
        assert calc.somar(1, 2) == 3

    # somar — caminho de erro (tipo inválido)
    def test_caminho_soma_erro(self, calc):
        with pytest.raises(TypeError):
            calc.somar("a", 1)

    # subtrair — caminho normal
    def test_caminho_subtrair_normal(self, calc):
        assert calc.subtrair(5, 3) == 2

    # subtrair — caminho de erro
    def test_caminho_subtrair_erro(self, calc):
        with pytest.raises(TypeError):
            calc.subtrair(None, 1)

    # multiplicar — caminho normal
    def test_caminho_multiplicar_normal(self, calc):
        assert calc.multiplicar(3, 4) == 12

    # multiplicar — caminho de erro
    def test_caminho_multiplicar_erro(self, calc):
        with pytest.raises(TypeError):
            calc.multiplicar("x", 1)

    # dividir — caminho normal
    def test_caminho_divisao_normal(self, calc):
        assert calc.dividir(10, 2) == 5.0

    # dividir — caminho divisão por zero
    def test_caminho_divisao_por_zero(self, calc):
        with pytest.raises(ValueError):
            calc.dividir(10, 0)

    # dividir — caminho tipo inválido
    def test_caminho_divisao_tipo_invalido(self, calc):
        with pytest.raises(TypeError):
            calc.dividir("10", 2)

    # potencia — caminho normal
    def test_caminho_potencia_normal(self, calc):
        assert calc.potencia(2, 3) == 8

    # potencia — caminho de erro
    def test_caminho_potencia_erro(self, calc):
        with pytest.raises(TypeError):
            calc.potencia("2", 3)