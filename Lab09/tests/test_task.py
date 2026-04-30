"""
Testes unitários da classe Task.

A classe Task não possui dependências externas, então nenhum mock é necessário.
Foco: verificar estado (atributos após criação) e ciclo de vida (transições de status).
"""
import pytest
from datetime import datetime, timedelta
from task_manager.task import Task, Priority, Status


# ──────────────────────────────────────────────
# FIXTURE – Setup: cria objeto em estado inicial válido antes de cada teste
# ──────────────────────────────────────────────

@pytest.fixture
def task_valida():
    """Cria uma task válida com prazo futuro para ser reutilizada nos testes."""
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Estudar", "Python", Priority.ALTA, prazo)


# ──────────────────────────────────────────────
# TESTE 1 – Estado inicial
# Verifica que todos os atributos foram atribuídos corretamente
# e que o status padrão é PENDENTE.
# ──────────────────────────────────────────────

def test_estado_inicial(task_valida):
    """Após criação válida, todos os atributos devem estar corretos e status = PENDENTE."""
    # Tipo: unitário
    task_valida.validar()  # não deve lançar erro

    assert task_valida.id is None
    assert task_valida.titulo == "Estudar"
    assert task_valida.descricao == "Python"
    assert task_valida.prioridade == Priority.ALTA
    assert task_valida.status == Status.PENDENTE  # estado padrão


# ──────────────────────────────────────────────
# TESTE 2 – Validação: título inválido (menos de 3 caracteres)
# Deve lançar ValueError conforme contrato de validar().
# ──────────────────────────────────────────────

def test_titulo_curto_invalido():
    """Título com menos de 3 caracteres deve lançar ValueError."""
    # Tipo: unitário
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "Descrição", Priority.BAIXA, prazo)

    with pytest.raises(ValueError):
        task.validar()


# ──────────────────────────────────────────────
# TESTE 3 – Validação: prazo no passado
# Deve lançar ValueError conforme contrato de validar().
# ──────────────────────────────────────────────

def test_prazo_no_passado_invalido():
    """Prazo com data passada deve lançar ValueError."""
    # Tipo: unitário
    prazo_passado = datetime.now() - timedelta(days=1)
    task = Task(None, "Tarefa", "Descrição", Priority.MEDIA, prazo_passado)

    with pytest.raises(ValueError):
        task.validar()


# ──────────────────────────────────────────────
# TESTE 4 – Ciclo de vida: transição válida de status
# Altera o status de PENDENTE para EM_PROGRESSO e verifica o novo estado.
# ──────────────────────────────────────────────

def test_ciclo_vida_transicao_valida(task_valida):
    """Deve ser possível alterar status de PENDENTE para EM_PROGRESSO."""
    # Tipo: unitário
    assert task_valida.status == Status.PENDENTE  # estado inicial

    task_valida.status = Status.EM_PROGRESSO

    assert task_valida.status == Status.EM_PROGRESSO  # estado mudou


# ──────────────────────────────────────────────
# TESTE 5 – Ciclo de vida: transição inválida de status
# Tentar definir um status com valor fora do enum deve lançar ValueError.
# ──────────────────────────────────────────────

def test_ciclo_vida_transicao_invalida(task_valida):
    """Atribuir um valor inválido ao status deve lançar ValueError."""
    # Tipo: unitário
    with pytest.raises(ValueError):
        task_valida.status = "invalido"  # string fora do enum


# ──────────────────────────────────────────────
# TESTE 6 – Ciclo de vida: transição completa PENDENTE → EM_PROGRESSO → CONCLUIDA
# Verifica a sequência completa de transições de estado.
# ──────────────────────────────────────────────

def test_ciclo_vida_transicao_completa(task_valida):
    """Deve ser possível percorrer todas as transições de status válidas."""
    # Tipo: unitário
    assert task_valida.status == Status.PENDENTE

    task_valida.status = Status.EM_PROGRESSO
    assert task_valida.status == Status.EM_PROGRESSO

    task_valida.status = Status.CONCLUIDA
    assert task_valida.status == Status.CONCLUIDA


# ──────────────────────────────────────────────
# TESTE 7 – Validação: título com exatamente 3 caracteres (limite mínimo válido)
# ──────────────────────────────────────────────

def test_titulo_com_exatamente_3_caracteres_valido():
    """Título com exatamente 3 caracteres deve ser considerado válido."""
    # Tipo: unitário
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "abc", "Descrição", Priority.MEDIA, prazo)

    task.validar()  # não deve lançar erro
    assert task.titulo == "abc"


# ──────────────────────────────────────────────
# TESTE 8 – Estado: prioridade é atribuída corretamente
# Verifica os diferentes níveis de prioridade.
# ──────────────────────────────────────────────

@pytest.mark.parametrize("prioridade", [Priority.BAIXA, Priority.MEDIA, Priority.ALTA])
def test_prioridade_atribuida_corretamente(prioridade):
    """Todos os níveis de prioridade devem ser atribuídos corretamente."""
    # Tipo: unitário
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "Tarefa", "Descrição", prioridade, prazo)

    assert task.prioridade == prioridade
