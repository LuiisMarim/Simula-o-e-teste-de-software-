"""
Testes de componente da classe TaskRepository.

TaskRepository é testado com sua lógica interna real,
mas a dependência externa (InMemoryStorage) é substituída por um mock.

Diferença entre stub e mock nesta atividade:
- Stub: configura return_value sem verificar chamada (só fornece resposta fixa).
- Mock: usa assert_called_* para verificar se e como o método foi chamado.
"""
import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock
from task_manager.task import Task, Priority, Status
from task_manager.repository import TaskRepository


# ──────────────────────────────────────────────
# FIXTURES – Setup
# ──────────────────────────────────────────────

@pytest.fixture
def mock_storage():
    """Cria um mock do InMemoryStorage para isolar a dependência externa."""
    return Mock()


@pytest.fixture
def repo(mock_storage):
    """Cria um TaskRepository com o storage mockado."""
    return TaskRepository(mock_storage)


@pytest.fixture
def task():
    """Cria uma task válida para ser usada nos testes."""
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Teste", "Descrição da tarefa", Priority.BAIXA, prazo)


# ──────────────────────────────────────────────
# TESTE 1 – Estado: save atribui ID à task
# Após save(), verifica que task.id foi definido (teste de estado + interação entre métodos).
# ──────────────────────────────────────────────

def test_save_atribui_id(repo, task):
    """Após save(), a task deve ter id=1 (primeiro ID atribuído)."""
    resultado = repo.save(task)

    assert resultado.id == 1  # estado mudou: id foi atribuído


# ──────────────────────────────────────────────
# TESTE 2 – Mock: save chama storage.add com os argumentos corretos
# Verifica que storage.add foi chamado exatamente uma vez com id=1 e a task.
# ──────────────────────────────────────────────

def test_save_chama_storage_add(repo, task, mock_storage):
    """save() deve chamar storage.add exatamente uma vez com (1, task)."""
    repo.save(task)

    mock_storage.add.assert_called_once_with(1, task)  # mock com assert


# ──────────────────────────────────────────────
# TESTE 3 – Stub: find_by_id delega ao storage
# Configura mock_storage.get.return_value e verifica que o repositório retorna o objeto correto.
# ──────────────────────────────────────────────

def test_find_by_id_usa_storage(repo, task, mock_storage):
    """find_by_id() deve delegar ao storage.get() e retornar o objeto correto."""
    mock_storage.get.return_value = task  # stub: configura retorno fixo

    resultado = repo.find_by_id(1)

    assert resultado == task  # verifica que o repositório retornou o objeto correto


# ──────────────────────────────────────────────
# TESTE 4 – Sequência: save seguido de find_by_id
# Verifica a colaboração entre métodos (salvar e depois recuperar).
# ──────────────────────────────────────────────

def test_sequencia_save_e_find_by_id(repo, task, mock_storage):
    """Após save(), find_by_id() deve retornar a mesma task salva."""
    # Configura stub: storage.get retorna a task após ser salva
    mock_storage.get.return_value = task

    # Sequência de operações
    task_salva = repo.save(task)
    task_encontrada = repo.find_by_id(task_salva.id)

    # Verifica colaboração entre métodos
    assert task_encontrada == task_salva
    mock_storage.add.assert_called_once()   # save chamou add
    mock_storage.get.assert_called_once()   # find_by_id chamou get


# ──────────────────────────────────────────────
# TESTE 5 – Isolamento: find_all retorna lista vazia quando storage não tem itens
# ──────────────────────────────────────────────

def test_find_all_retorna_lista_vazia(repo, mock_storage):
    """Quando o storage não tem itens, find_all() deve retornar lista vazia."""
    mock_storage.get_all.return_value = []  # stub: storage vazio

    resultado = repo.find_all()

    assert resultado == []


# ──────────────────────────────────────────────
# TESTE 6 – Mock: delete chama storage.delete com o ID correto
# ──────────────────────────────────────────────

def test_delete_chama_storage_delete(repo, mock_storage):
    """delete() deve chamar storage.delete exatamente uma vez com o ID correto."""
    mock_storage.delete.return_value = True  # stub: retorna sucesso

    resultado = repo.delete(1)

    mock_storage.delete.assert_called_once_with(1)  # mock com assert
    assert resultado is True


# ──────────────────────────────────────────────
# TESTE 7 – Estado: save incrementa _next_id a cada chamada
# Verifica que o repositório mantém controle correto dos IDs sequenciais.
# ──────────────────────────────────────────────

def test_save_incrementa_id_sequencialmente(mock_storage):
    """Cada chamada a save() deve atribuir IDs sequenciais (1, 2, 3...)."""
    repo = TaskRepository(mock_storage)
    prazo = datetime.now() + timedelta(days=1)

    task1 = Task(None, "Tarefa 1", "Desc", Priority.BAIXA, prazo)
    task2 = Task(None, "Tarefa 2", "Desc", Priority.MEDIA, prazo)
    task3 = Task(None, "Tarefa 3", "Desc", Priority.ALTA, prazo)

    repo.save(task1)
    repo.save(task2)
    repo.save(task3)

    assert task1.id == 1
    assert task2.id == 2
    assert task3.id == 3


# ──────────────────────────────────────────────
# TESTE 8 – Stub: find_by_id retorna None quando task não existe
# ──────────────────────────────────────────────

def test_find_by_id_retorna_none_quando_nao_existe(repo, mock_storage):
    """find_by_id() deve retornar None quando o ID não existe no storage."""
    mock_storage.get.return_value = None  # stub: task não encontrada

    resultado = repo.find_by_id(999)

    assert resultado is None
