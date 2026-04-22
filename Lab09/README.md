# Task Manager – CC8550 Atividade 09

Sistema de Gerenciamento de Tarefas simples em Python com testes automatizados
orientados a objetos e componentes (pytest).

## Descrição

O sistema permite criar, listar, buscar, atualizar e deletar tarefas com título,
descrição, prioridade e prazo. Os testes exercitam explicitamente os conceitos
da Aula 09: testes de estado, fixtures, stubs, mocks, ciclo de vida do objeto
e distinção entre testes unitários e de componente.

## Como instalar

```bash
pip install -r requirements.txt
```

## Como testar

```bash
pytest -v
```

Executar com cobertura:

```bash
pytest --cov=task_manager
```

## Estrutura do projeto

```
task_manager/
    __init__.py
    task.py         # Enums Priority, Status e classe Task
    storage.py      # Classe InMemoryStorage
    repository.py   # Classe TaskRepository
    service.py      # Classe TaskService (bônus)
tests/
    __init__.py
    test_task.py        # Testes unitários de Task (8 testes)
    test_repository.py  # Testes de componente de TaskRepository (8 testes)
requirements.txt
README.md
```

## Conceitos cobertos pelos testes

- **Testes de estado**: verificam atributos do objeto após chamadas de método.
- **Fixtures**: setup automático com `@pytest.fixture` antes de cada teste.
- **Stubs**: `return_value` configurado para fornecer resposta fixa sem verificar chamada.
- **Mocks**: `assert_called_once_with()` para verificar se e como o colaborador foi chamado.
- **Ciclo de vida**: transições de status válidas e inválidas.
- **Teste unitário** (`test_task.py`): classe Task isolada, sem dependências, sem mocks.
- **Teste de componente** (`test_repository.py`): TaskRepository com lógica interna real e storage mockado.
