from task_manager.task import Task, Priority, Status
from task_manager.repository import TaskRepository
from datetime import datetime


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def criar_tarefa(self, titulo: str, descricao: str, prioridade: Priority, prazo: datetime) -> Task:
        """Cria, valida e salva uma nova tarefa. Retorna a task salva."""
        task = Task(None, titulo, descricao, prioridade, prazo)
        task.validar()
        return self.repository.save(task)

    def listar_todas(self) -> list:
        """Retorna todas as tasks."""
        return self.repository.find_all()

    def atualizar_status(self, id: int, status: Status) -> Task:
        """Atualiza o status de uma task pelo ID. Retorna a task atualizada ou None."""
        task = self.repository.find_by_id(id)
        if task is None:
            return None
        task.status = status
        return task
