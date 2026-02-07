import pytest
import sys
sys.path.insert(0, '/workspaces/Simula-o-e-teste-de-software-/Lab01/src')

from notas import (
    validar_nota,
    calcular_media,
    obter_situacao,
    calcular_estatisticas,
    normalizar_notas
)


class TestValidarNota:
    """Testes para a função validar_nota"""
    
    def test_nota_valida_minima(self):
        """Testa se nota 0 é válida"""
        assert validar_nota(0) == True
    
    def test_nota_valida_maxima(self):
        """Testa se nota 10 é válida"""
        assert validar_nota(10) == True
    
    def test_nota_valida_no_meio(self):
        """Testa se nota no intervalo é válida"""
        assert validar_nota(5.5) == True
    
    def test_nota_invalida_negativa(self):
        """Testa se nota negativa é inválida"""
        assert validar_nota(-1) == False
    
    def test_nota_invalida_maior_que_10(self):
        """Testa se nota maior que 10 é inválida"""
        assert validar_nota(11) == False


class TestCalcularMedia:
    """Testes para a função calcular_media"""
    
    def test_media_com_notas_validas(self):
        """Testa cálculo da média com notas válidas"""
        assert calcular_media([5, 7, 9]) == pytest.approx(7.0)
    
    def test_media_com_uma_nota(self):
        """Testa cálculo da média com uma única nota"""
        assert calcular_media([8]) == 8
    
    def test_media_com_notas_iguais(self):
        """Testa cálculo da média com todas as notas iguais"""
        assert calcular_media([6, 6, 6]) == 6
    
    def test_media_lista_vazia(self):
        """Testa se levanta exceção com lista vazia"""
        with pytest.raises(ValueError, match="Lista vazia"):
            calcular_media([])


class TestObterSituacao:
    """Testes para a função obter_situacao"""
    
    def test_situacao_reprovado_media_abaixo_de_5(self):
        """Testa se media abaixo de 5 retorna Reprovado"""
        assert obter_situacao(4) == 'Reprovado'
    
    def test_situacao_reprovado_media_zero(self):
        """Testa se media zero retorna Reprovado"""
        assert obter_situacao(0) == 'Reprovado'
    
    def test_situacao_aprovado_media_5(self):
        """Testa se media 5 retorna Aprovado"""
        assert obter_situacao(5) == 'Aprovado'
    
    def test_situacao_aprovado_media_acima_de_5(self):
        """Testa se media acima de 5 retorna Aprovado"""
        assert obter_situacao(7.5) == 'Aprovado'
    
    def test_situacao_aprovado_media_10(self):
        """Testa se media 10 retorna Aprovado"""
        assert obter_situacao(10) == 'Aprovado'
    
    def test_situacao_media_invalida(self):
        """Testa se levanta exceção com média maior que 10"""
        with pytest.raises(ValueError, match="Média inválida"):
            obter_situacao(11)


class TestCalcularEstatisticas:
    """Testes para a função calcular_estatisticas"""
    
    def test_estatisticas_lista_vazia(self):
        """Testa estatísticas com lista vazia"""
        resultado = calcular_estatisticas([])
        assert resultado['quantidade'] == 0
        assert resultado['media'] == 0
        assert resultado['maior'] is None
        assert resultado['menor'] is None
    
    def test_estatisticas_com_uma_nota(self):
        """Testa estatísticas com uma única nota"""
        resultado = calcular_estatisticas([7])
        assert resultado['quantidade'] == 1
        assert resultado['media'] == 7
        assert resultado['maior'] == 7
        assert resultado['menor'] == 7
        assert resultado['aprovados'] == 1
        assert resultado['reprovados'] == 0
    
    def test_estatisticas_multiplas_notas(self):
        """Testa estatísticas com múltiplas notas"""
        resultado = calcular_estatisticas([3, 5, 7, 9, 2])
        assert resultado['quantidade'] == 5
        assert resultado['media'] == pytest.approx(5.2)
        assert resultado['maior'] == 9
        assert resultado['menor'] == 2
        assert resultado['aprovados'] == 2
        assert resultado['reprovados'] == 2
    
    def test_estatisticas_notas_todas_aprovado(self):
        """Testa estatísticas com todas as notas acima de 5"""
        resultado = calcular_estatisticas([6, 7, 8, 9])
        assert resultado['aprovados'] == 4
        assert resultado['reprovados'] == 0


class TestNormalizarNotas:
    """Testes para a função normalizar_notas"""
    
    def test_normaliza_com_divisor_10(self):
        """Testa normalização com divisor 10"""
        resultado = normalizar_notas([5, 10], 10)
        assert resultado == pytest.approx([5, 10])
    
    def test_normaliza_com_divisor_100(self):
        """Testa normalização com divisor 100"""
        resultado = normalizar_notas([50, 100], 100)
        assert resultado == pytest.approx([5, 10])
    
    def test_normaliza_lista_vazia(self):
        """Testa normalização com lista vazia"""
        resultado = normalizar_notas([], 10)
        assert resultado == []
    
    def test_normaliza_com_max_zero(self):
        """Testa se levanta exceção com max igual a zero"""
        with pytest.raises(ValueError, match="O valor máximo deve ser maior que zero"):
            normalizar_notas([5], 0)
    
    def test_normaliza_com_max_negativo(self):
        """Testa se levanta exceção com max negativo"""
        with pytest.raises(ValueError, match="O valor máximo deve ser maior que zero"):
            normalizar_notas([5], -10) 