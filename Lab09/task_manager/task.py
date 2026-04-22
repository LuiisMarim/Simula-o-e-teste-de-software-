from enum import IntEnum, Enum
from datetime import datetime


class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3


class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"


class Task:
    def __init__(self, id, titulo: str, descricao: str, prioridade: Priority, prazo: datetime):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.status = Status.PENDENTE

    def validar(self):
        if len(self.titulo) < 3:
            raise ValueError(
                f"Título deve ter pelo menos 3 caracteres. Atual: '{self.titulo}'"
            )
        if self.prazo < datetime.now():
            raise ValueError(
                f"Prazo não pode ser uma data passada. Prazo: {self.prazo}"
            )

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        if not isinstance(valor, Status):
            raise ValueError(
                f"Status inválido: '{valor}'. Use um valor do enum Status."
            )
        self._status = valor

    def __repr__(self):
        return (
            f"Task(id={self.id}, titulo='{self.titulo}', "
            f"prioridade={self.prioridade.name}, status={self.status.value})"
        )
