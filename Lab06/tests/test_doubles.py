"""
Parte 3 — Test Doubles: Stub e Mock
Explora o uso de MagicMock para testar a Calculadora em isolamento.
"""
from unittest.mock import MagicMock

import pytest

from src.calculadora import Calculadora


# ============================================================
# 4.1 — Stub: controlando o estado do repositório
# ============================================================
class TestComStub:
    """Testa a Calculadora sem depender da implementação real do repositório.
    O stub (MagicMock sem asserts de chamada) retorna valores pré-definidos."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.stub_repo = MagicMock()
        self.calc = Calculadora(self.stub_repo)

    def test_soma_stub_repositorio(self):
        # stub: salvar() não faz nada de verdade
        resultado = self.calc.somar(10, 5)
        assert resultado == 15

    def test_stub_repositorio_nao_precisa_estar_pronto(self):
        # A calculadora pode ser testada mesmo antes do repositório existir
        self.stub_repo.total.return_value = 0
        resultado = self.calc.multiplicar(3, 7)
        assert resultado == 21

    def test_subtrair_com_stub(self):
        assert self.calc.subtrair(20, 8) == 12

    def test_dividir_com_stub(self):
        assert self.calc.dividir(15, 3) == 5.0

    def test_potencia_com_stub(self):
        assert self.calc.potencia(5, 2) == 25

    def test_stub_permite_testar_ultimo_resultado(self):
        self.calc.somar(100, 200)
        assert self.calc.obter_ultimo_resultado() == 300


# ============================================================
# 4.2 — Mock: verificando o comportamento (interação)
# ============================================================
class TestComMock:
    """Verifica se e como a Calculadora chama o repositório."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.mock_repo = MagicMock()
        self.calc = Calculadora(self.mock_repo)

    # --- salvar chamado após cada operação ---
    def test_mock_salvar_chamado_apos_soma(self):
        self.calc.somar(4, 6)
        self.mock_repo.salvar.assert_called_once()

    def test_mock_salvar_chamado_apos_subtrair(self):
        self.calc.subtrair(10, 3)
        self.mock_repo.salvar.assert_called_once()

    def test_mock_salvar_chamado_apos_multiplicar(self):
        self.calc.multiplicar(2, 5)
        self.mock_repo.salvar.assert_called_once()

    def test_mock_salvar_chamado_apos_dividir(self):
        self.calc.dividir(20, 4)
        self.mock_repo.salvar.assert_called_once()

    def test_mock_salvar_chamado_apos_potencia(self):
        self.calc.potencia(3, 2)
        self.mock_repo.salvar.assert_called_once()

    # --- verifica argumento exato passado a salvar() ---
    def test_mock_argumento_soma(self):
        self.calc.somar(4, 6)
        self.mock_repo.salvar.assert_called_once_with("4 + 6 = 10")

    def test_mock_argumento_subtrair(self):
        self.calc.subtrair(10, 3)
        self.mock_repo.salvar.assert_called_once_with("10 - 3 = 7")

    def test_mock_argumento_multiplicar(self):
        self.calc.multiplicar(4, 5)
        self.mock_repo.salvar.assert_called_once_with("4 * 5 = 20")

    def test_mock_argumento_dividir(self):
        self.calc.dividir(10, 4)
        self.mock_repo.salvar.assert_called_once_with("10 / 4 = 2.5")

    def test_mock_argumento_potencia(self):
        """Após correção do bug, potencia registra com '**'."""
        self.calc.potencia(2, 3)
        self.mock_repo.salvar.assert_called_once_with("2 ** 3 = 8")

    # --- salvar NÃO chamado quando há exceção ---
    def test_mock_salvar_nao_chamado_em_excecao_tipo(self):
        with pytest.raises(TypeError):
            self.calc.somar("x", 1)
        self.mock_repo.salvar.assert_not_called()

    def test_mock_salvar_nao_chamado_em_excecao_divisao_zero(self):
        with pytest.raises(ValueError):
            self.calc.dividir(10, 0)
        self.mock_repo.salvar.assert_not_called()

    def test_mock_salvar_nao_chamado_subtrair_tipo_invalido(self):
        with pytest.raises(TypeError):
            self.calc.subtrair(None, 1)
        self.mock_repo.salvar.assert_not_called()

    def test_mock_salvar_nao_chamado_multiplicar_tipo_invalido(self):
        with pytest.raises(TypeError):
            self.calc.multiplicar([], 2)
        self.mock_repo.salvar.assert_not_called()

    def test_mock_salvar_nao_chamado_potencia_tipo_invalido(self):
        with pytest.raises(TypeError):
            self.calc.potencia("a", 2)
        self.mock_repo.salvar.assert_not_called()

    # --- múltiplas chamadas ---
    def test_mock_multiplas_operacoes_contam_chamadas(self):
        self.calc.somar(1, 1)
        self.calc.somar(2, 2)
        assert self.mock_repo.salvar.call_count == 2


# ============================================================
# Detecção do Bug Original em potencia
# ============================================================
class TestDeteccaoBugPotencia:
    """Documenta como o mock detectou o bug intencional.

    BUG ORIGINAL (linha 45 do código fornecido):
        self.repositorio.salvar(f"{base} * {expoente} = {resultado}")
        O operador na string de histórico era '*' (multiplicação),
        mas deveria ser '**' (potenciação).

    CORREÇÃO APLICADA:
        self.repositorio.salvar(f"{base} ** {expoente} = {resultado}")

    O teste mock abaixo verifica que a string agora usa '**'.
    Se o bug estivesse presente, este teste falharia porque
    o argumento recebido seria "2 * 3 = 8" em vez de "2 ** 3 = 8".
    """

    def test_potencia_registra_operador_correto(self):
        mock_repo = MagicMock()
        calc = Calculadora(mock_repo)
        calc.potencia(2, 3)

        # Com o bug corrigido, deve ser "2 ** 3 = 8"
        args_chamada = mock_repo.salvar.call_args[0][0]
        assert "**" in args_chamada, (
            f"Esperava operador '**' na string de histórico, "
            f"mas obteve: '{args_chamada}'"
        )