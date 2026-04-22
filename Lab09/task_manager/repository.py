from task_manager.storage import InMemoryStorage


class TaskRepository:
    def __init__(self, storage: InMemoryStorage):
        self.storage = storage
        self._next_id = 1

    def save(self, task):
        """Atribui ID à task, salva no storage e retorna a task."""
        task.id = self._next_id
        self._next_id += 1
        self.storage.add(task.id, task)
        return task

    def find_by_id(self, id):
        """Busca e retorna task pelo ID, ou None se não encontrada."""
        return self.storage.get(id)

    def find_all(self):
        """Retorna lista de todas as tasks."""
        return self.storage.get_all()

    def delete(self, id):
        """Remove task pelo ID. Retorna True se removida, False caso contrário."""
        return self.storage.delete(id)
