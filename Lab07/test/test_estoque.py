import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from estoque import Estoque


# ============================================================
# ITERAÇÃO 1 — adicionar_produto (caso básico)
# ============================================================

# RED: Estoque não existe ainda; teste falha com ImportError/AttributeError.
# GREEN: Criar classe Estoque com adicionar_produto e consultar_quantidade.
# REFACTOR: (nada a refatorar ainda)

class TestAdicionarProduto:

    def test_adicionar_produto_novo(self):
        """Adicionar um produto novo deve registrar a quantidade informada."""
        e = Estoque()
        e.adicionar_produto("Caneta", 10)
        assert e.consultar_quantidade("Caneta") == 10

    def test_adicionar_produto_existente_incrementa(self):
        """Adicionar produto já existente deve INCREMENTAR, não substituir."""
        e = Estoque()
        e.adicionar_produto("Caneta", 10)
        e.adicionar_produto("Caneta", 5)
        assert e.consultar_quantidade("Caneta") == 15

    def test_adicionar_quantidade_zero_levanta_excecao(self):
        """Quantidade <= 0 não é permitida ao adicionar."""
        e = Estoque()
        with pytest.raises(ValueError):
            e.adicionar_produto("Caneta", 0)

    def test_adicionar_quantidade_negativa_levanta_excecao(self):
        """Quantidade negativa não é permitida ao adicionar."""
        e = Estoque()
        with pytest.raises(ValueError):
            e.adicionar_produto("Caneta", -3)


# ============================================================
# ITERAÇÃO 2 — consultar_quantidade
# ============================================================

# RED: consultar_quantidade para produto inexistente não retorna 0 ainda.
# GREEN: Ajustar consultar_quantidade para retornar 0 se produto não existe.
# REFACTOR: (nada a refatorar)

class TestConsultarQuantidade:

    def test_consultar_produto_inexistente_retorna_zero(self):
        """Consultar produto que não existe deve retornar 0."""
        e = Estoque()
        assert e.consultar_quantidade("Lápis") == 0

    def test_consultar_produto_existente(self):
        """Consultar produto existente deve retornar a quantidade correta."""
        e = Estoque()
        e.adicionar_produto("Borracha", 7)
        assert e.consultar_quantidade("Borracha") == 7


# ============================================================
# ITERAÇÃO 3 — remover_produto
# ============================================================

# RED: método remover_produto não existe; teste falha com AttributeError.
# GREEN: Implementar remover_produto com validação de saldo e valor positivo.
# REFACTOR: Extrair validação de quantidade positiva em método auxiliar.

class TestRemoverProduto:

    def test_remover_produto_diminui_quantidade(self):
        """Remover unidades deve diminuir a quantidade no estoque."""
        e = Estoque()
        e.adicionar_produto("Caderno", 20)
        e.remover_produto("Caderno", 5)
        assert e.consultar_quantidade("Caderno") == 15

    def test_remover_mais_que_disponivel_levanta_excecao(self):
        """Não é possível remover mais do que o disponível."""
        e = Estoque()
        e.adicionar_produto("Caderno", 3)
        with pytest.raises(ValueError):
            e.remover_produto("Caderno", 10)

    def test_remover_produto_inexistente_levanta_excecao(self):
        """Remover produto que não existe deve levantar exceção."""
        e = Estoque()
        with pytest.raises(ValueError):
            e.remover_produto("Fantasma", 1)

    def test_remover_quantidade_zero_levanta_excecao(self):
        """Quantidade <= 0 não é permitida ao remover."""
        e = Estoque()
        e.adicionar_produto("Caderno", 10)
        with pytest.raises(ValueError):
            e.remover_produto("Caderno", 0)

    def test_remover_quantidade_negativa_levanta_excecao(self):
        """Quantidade negativa não é permitida ao remover."""
        e = Estoque()
        e.adicionar_produto("Caderno", 10)
        with pytest.raises(ValueError):
            e.remover_produto("Caderno", -2)


# ============================================================
# ITERAÇÃO 4 — listar_produtos
# ============================================================

# RED: método listar_produtos não existe; teste falha com AttributeError.
# GREEN: Implementar listar_produtos filtrando quantidade > 0.
# REFACTOR: (nada a refatorar)

class TestListarProdutos:

    def test_listar_estoque_vazio(self):
        """Estoque vazio deve retornar lista vazia."""
        e = Estoque()
        assert e.listar_produtos() == []

    def test_listar_com_produtos(self):
        """Deve listar apenas produtos com quantidade > 0."""
        e = Estoque()
        e.adicionar_produto("Caneta", 5)
        e.adicionar_produto("Lápis", 3)
        resultado = e.listar_produtos()
        assert sorted(resultado) == ["Caneta", "Lápis"]

    def test_listar_exclui_produtos_zerados(self):
        """Produtos cuja quantidade chegou a 0 não devem aparecer na lista."""
        e = Estoque()
        e.adicionar_produto("Caneta", 5)
        e.adicionar_produto("Lápis", 3)
        e.remover_produto("Caneta", 5)
        assert e.listar_produtos() == ["Lápis"]


# ============================================================
# ITERAÇÃO 5 — produto_mais_estocado
# ============================================================

# RED: método produto_mais_estocado não existe; teste falha com AttributeError.
# GREEN: Implementar retornando o nome com maior quantidade, ou None.
# REFACTOR: Consolidar docstrings e type hints na classe.

class TestProdutoMaisEstocado:

    def test_mais_estocado_estoque_vazio_retorna_none(self):
        """Estoque vazio deve retornar None."""
        e = Estoque()
        assert e.produto_mais_estocado() is None

    def test_mais_estocado_com_um_produto(self):
        """Com um único produto, ele deve ser retornado."""
        e = Estoque()
        e.adicionar_produto("Caneta", 10)
        assert e.produto_mais_estocado() == "Caneta"

    def test_mais_estocado_com_varios_produtos(self):
        """Deve retornar o produto com maior quantidade."""
        e = Estoque()
        e.adicionar_produto("Caneta", 10)
        e.adicionar_produto("Lápis", 50)
        e.adicionar_produto("Borracha", 25)
        assert e.produto_mais_estocado() == "Lápis"

    def test_mais_estocado_ignora_zerados(self):
        """Produtos com quantidade 0 não devem ser considerados."""
        e = Estoque()
        e.adicionar_produto("Caneta", 5)
        e.adicionar_produto("Lápis", 5)
        e.remover_produto("Lápis", 5)
        assert e.produto_mais_estocado() == "Caneta"