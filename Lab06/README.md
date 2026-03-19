# Projeto Calculadora — Atividade 06

**CC8550 — Simulação e Teste de Software**  
Centro Universitário FEI — Prof. Luciano Rossi

## Descrição

Sistema de calculadora com persistência de histórico, desenvolvido para aplicação prática de testes de unidade, integração e test doubles (stubs e mocks) utilizando **pytest**.

## Estrutura do Projeto

```
projeto_calculadora/
├── src/
│   ├── __init__.py
│   ├── calculadora.py      # Módulo da calculadora (bug corrigido)
│   └── repositorio.py      # Módulo do repositório de histórico
├── tests/
│   ├── __init__.py
│   ├── test_unidade.py      # Parte 1 — Testes de unidade
│   ├── test_integracao.py   # Parte 2 — Testes de integração
│   └── test_doubles.py      # Parte 3 — Stubs e mocks
├── requirements.txt
├── README.md
└── relatorio.md
```

## Como Executar

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar todos os testes com verbose
pytest -v

# Medir cobertura
pytest --cov=src --cov-report=term-missing

# Gerar relatório HTML de cobertura
pytest --cov=src --cov-report=html
# O relatório fica em htmlcov/index.html
```

## Bug Encontrado e Corrigido

No método `potencia` de `calculadora.py`, a string de histórico usava o operador `*` (multiplicação) em vez de `**` (potenciação):

**Antes (com bug):**
```python
self.repositorio.salvar(f"{base} * {expoente} = {resultado}")
```

**Depois (corrigido):**
```python
self.repositorio.salvar(f"{base} ** {expoente} = {resultado}")
```