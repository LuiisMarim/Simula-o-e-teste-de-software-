class InMemoryStorage:
    def __init__(self):
        self._data = {}

    def add(self, id, item):
        """Adiciona item com chave id."""
        self._data[id] = item

    def get(self, id):
        """Retorna item ou None se não encontrado."""
        return self._data.get(id)

    def get_all(self):
        """Retorna lista com todos os valores."""
        return list(self._data.values())

    def delete(self, id):
        """Remove item. Retorna True se removido, False se não existia."""
        if id in self._data:
            del self._data[id]
            return True
        return False

    def clear(self):
        """Limpa todos os dados."""
        self._data.clear()
