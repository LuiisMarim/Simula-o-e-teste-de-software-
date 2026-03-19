"""
Parte 2 — Testes de Integração com Repositório Real
Testa Calculadora + HistoricoRepositorio juntos, sem stubs.
"""
import pytest

from src.calculadora import Calculadora
from src.repositorio import HistoricoRepositorio


@pytest.fixture
def sistema():
    """Retorna tupla (calculadora, repositorio) com implementação real."""
    repo = HistoricoRepositorio()
    calc = Calculadora(repo)
    return calc, repo


# ============================================================
# 3.1 — Operações Sequenciais
# ============================================================
class TestOperacoesSequenciais:
    """Verifica se múltiplas operações encadeadas produzem estado correto."""

    def test_operacoes_sequenciais_basicas(self, sistema):
        calc, repo = sistema
        # 2 + 3 = 5, depois 5 * 4 = 20, depois 20 / 2 = 10
        calc.somar(2, 3)
        calc.multiplicar(calc.obter_ultimo_resultado(), 4)
        calc.dividir(calc.obter_ultimo_resultado(), 2)

        assert calc.obter_ultimo_resultado() == 10
        assert repo.total() == 3

    def test_operacoes_sequenciais_com_potencia(self, sistema):
        calc, repo = sistema
        # 3 ** 2 = 9, depois 9 - 1 = 8
        calc.potencia(3, 2)
        calc.subtrair(calc.obter_ultimo_resultado(), 1)

        assert calc.obter_ultimo_resultado() == 8
        assert repo.total() == 2

    def test_operacoes_sequenciais_todas_operacoes(self, sistema):
        calc, repo = sistema
        calc.somar(10, 5)        # 15
        calc.subtrair(calc.obter_ultimo_resultado(), 3)   # 12
        calc.multiplicar(calc.obter_ultimo_resultado(), 2) # 24
        calc.dividir(calc.obter_ultimo_resultado(), 6)     # 4
        calc.potencia(calc.obter_ultimo_resultado(), 3)    # 64

        assert calc.obter_ultimo_resultado() == 64
        assert repo.total() == 5


# ============================================================
# 3.2 — Consistência do Histórico
# ============================================================
class TestConsistenciaHistorico:
    """Verifica se o histórico registra as operações corretamente."""

    def test_historico_registra_formato_correto(self, sistema):
        calc, repo = sistema
        calc.somar(2, 3)
        calc.multiplicar(4, 5)
        registros = repo.listar()
        assert "2 + 3 = 5" in registros
        assert "4 * 5 = 20" in registros

    def test_limpar_historico(self, sistema):
        calc, repo = sistema
        calc.somar(1, 1)
        repo.limpar()
        assert repo.total() == 0

    def test_historico_subtracão(self, sistema):
        calc, repo = sistema
        calc.subtrair(10, 3)
        assert "10 - 3 = 7" in repo.listar()

    def test_historico_divisao(self, sistema):
        calc, repo = sistema
        calc.dividir(10, 4)
        assert "10 / 4 = 2.5" in repo.listar()

    def test_historico_potencia_formato_corrigido(self, sistema):
        """Após a correção do bug, potencia deve registrar com '**'."""
        calc, repo = sistema
        calc.potencia(2, 3)
        registros = repo.listar()
        assert "2 ** 3 = 8" in registros
        # Garante que o operador errado '*' não aparece sozinho
        assert "2 * 3 = 8" not in registros

    def test_historico_ordem_preservada(self, sistema):
        calc, repo = sistema
        calc.somar(1, 1)
        calc.somar(2, 2)
        calc.somar(3, 3)
        registros = repo.listar()
        assert registros[0] == "1 + 1 = 2"
        assert registros[1] == "2 + 2 = 4"
        assert registros[2] == "3 + 3 = 6"

    def test_limpar_e_recriar_historico(self, sistema):
        calc, repo = sistema
        calc.somar(1, 1)
        repo.limpar()
        calc.multiplicar(3, 3)
        assert repo.total() == 1
        assert "3 * 3 = 9" in repo.listar()