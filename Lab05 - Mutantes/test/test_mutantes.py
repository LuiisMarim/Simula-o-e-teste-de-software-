import pytest
import sys
sys.path.insert(0, '/workspaces/Simula-o-e-teste-de-software-/Lab05 - Mutantes/src')
from mutantes import (
    soma_m1 as soma,
    is_par_m3 as is_par,
    maior_m5 as maior,
    fatorial_m8 as fatorial,
    classificar_nota_m10 as classificar_nota
)
# --- Testes para soma ---
def test_soma_positivos():
    assert soma(3, 4) == 7


def test_soma_negativos():
    assert soma(-2, -3) == -5


# --- Testes para is_par ---
def test_is_par_par():
    assert is_par(4) is True


def test_is_par_impar():
    assert is_par(7) is False


# --- Testes para maior ---
def test_maior_primeiro_maior():
    assert maior(10, 5) == 10


def test_maior_segundo_maior():
    assert maior(3, 9) == 9


# --- Testes para fatorial ---
def test_fatorial_zero():
    assert fatorial(0) == 1


def test_fatorial_cinco():
    assert fatorial(5) == 120


def test_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-1)


# --- Teste para classificar_nota ---
def test_classificar_nota_aprovado():
    assert classificar_nota(8) == "Aprovado"



# ============================================================
# Resultado manual
# ============================================================

# Mutantes totais: 10
# Mutantes mortos: 7
# Mutantes sobreviventes: 3

# Fórmula:
# Mutation Score = (Mutantes Mortos / Mutantes Totais) * 100

# Cálculo:
# Mutation Score = (7 / 10) * 100

# Resultado final:
# Mutation Score = 70%