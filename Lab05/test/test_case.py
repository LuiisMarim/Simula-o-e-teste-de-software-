import pytest
from case import soma, is_par, maior, fatorial, classificar_nota


def test_soma_positivos():
    assert soma(3, 4) == 7


def test_soma_negativos():
    assert soma(-2, -3) == -5


def test_is_par_par():
    assert is_par(4) is True


def test_is_par_impar():
    assert is_par(7) is False


def test_maior_primeiro_maior():
    assert maior(10, 5) == 10


def test_maior_segundo_maior():
    assert maior(3, 9) == 9


def test_fatorial_zero():
    assert fatorial(0) == 1


def test_fatorial_cinco():
    assert fatorial(5) == 120


def test_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-1)


def test_classificar_nota_aprovado():
    assert classificar_nota(8) == "Aprovado"