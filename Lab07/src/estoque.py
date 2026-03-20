from typing import Optional


class Estoque:
    """Gerencia um estoque de produtos com operações de adição,
    remoção, consulta e listagem."""

    def __init__(self) -> None:
        self._produtos: dict[str, int] = {}

    # ----------------------------------------------------------
    # Método auxiliar (extraído na fase REFACTOR da iteração 3)
    # ----------------------------------------------------------
    def _validar_quantidade_positiva(self, quantidade: int, operacao: str) -> None:
        """Garante que a quantidade informada seja estritamente positiva."""
        if quantidade <= 0:
            raise ValueError(
                f"{operacao}: quantidade deve ser um valor positivo"
            )

    # ----------------------------------------------------------
    # ITERAÇÃO 1 — RED: test_adicionar_produto_novo falha (classe não existe)
    #              GREEN: implementação mínima abaixo
    #              REFACTOR: adicionar type hints e docstring
    # ----------------------------------------------------------
    def adicionar_produto(self, nome: str, quantidade: int) -> None:
        """Adiciona unidades de um produto ao estoque.

        Se o produto já existir, a quantidade é incrementada.

        Args:
            nome: nome do produto.
            quantidade: número de unidades a adicionar (deve ser > 0).

        Raises:
            ValueError: se quantidade <= 0.
        """
        self._validar_quantidade_positiva(quantidade, "Adição")
        self._produtos[nome] = self._produtos.get(nome, 0) + quantidade

    # ----------------------------------------------------------
    # ITERAÇÃO 2 — RED: test_consultar_produto_inexistente_retorna_zero falha
    #              GREEN: retornar 0 com dict.get
    #              REFACTOR: (nada a refatorar)
    # ----------------------------------------------------------
    def consultar_quantidade(self, nome: str) -> int:
        """Retorna a quantidade disponível de um produto.

        Args:
            nome: nome do produto.

        Returns:
            Quantidade em estoque, ou 0 se o produto não existir.
        """
        return self._produtos.get(nome, 0)

    # ----------------------------------------------------------
    # ITERAÇÃO 3 — RED: test_remover_produto_diminui_quantidade falha
    #              GREEN: implementar remoção com validações
    #              REFACTOR: extrair _validar_quantidade_positiva
    # ----------------------------------------------------------
    def remover_produto(self, nome: str, quantidade: int) -> None:
        """Remove unidades de um produto do estoque.

        Args:
            nome: nome do produto.
            quantidade: número de unidades a remover (deve ser > 0).

        Raises:
            ValueError: se quantidade <= 0, produto inexistente ou
                        quantidade maior que o disponível.
        """
        self._validar_quantidade_positiva(quantidade, "Remoção")

        disponivel = self._produtos.get(nome, 0)
        if disponivel == 0:
            raise ValueError(f"Produto '{nome}' não encontrado no estoque")
        if quantidade > disponivel:
            raise ValueError(
                f"Estoque insuficiente de '{nome}': "
                f"disponível={disponivel}, solicitado={quantidade}"
            )

        self._produtos[nome] = disponivel - quantidade

    # ----------------------------------------------------------
    # ITERAÇÃO 4 — RED: test_listar_estoque_vazio falha
    #              GREEN: filtrar produtos com quantidade > 0
    #              REFACTOR: (nada a refatorar)
    # ----------------------------------------------------------
    def listar_produtos(self) -> list[str]:
        """Retorna os nomes dos produtos com quantidade > 0.

        Returns:
            Lista de nomes de produtos em estoque.
        """
        return [nome for nome, qtd in self._produtos.items() if qtd > 0]

    # ----------------------------------------------------------
    # ITERAÇÃO 5 — RED: test_mais_estocado_estoque_vazio_retorna_none falha
    #              GREEN: usar max() sobre produtos com qtd > 0
    #              REFACTOR: consolidar docstrings e type hints finais
    # ----------------------------------------------------------
    def produto_mais_estocado(self) -> Optional[str]:
        """Retorna o nome do produto com maior quantidade em estoque.

        Returns:
            Nome do produto, ou None se o estoque estiver vazio.
        """
        produtos_ativos = {n: q for n, q in self._produtos.items() if q > 0}
        if not produtos_ativos:
            return None
        return max(produtos_ativos, key=produtos_ativos.get)