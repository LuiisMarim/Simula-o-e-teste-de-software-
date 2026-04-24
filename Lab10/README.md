# Testes Não Funcionais — E-commerce Black Friday

Projeto prático em Python para a atividade de testes não funcionais de um e-commerce que será lançado na Black Friday.

## Estrutura

```text
src/
  ecommerce/
    app.py          # API FastAPI simulando o e-commerce
    metrics.py      # Cálculo de métricas não funcionais
test/
  conftest.py
  test_performance.py
  test_load.py
  test_stress.py
  test_scalability.py
  test_security.py
locustfile.py       # Carga realista com Locust
stress_locust.py    # Estresse/spike com Locust
requirements.txt
README.md
```

## Métricas implementadas

| Tipo de teste | Métrica | Meta |
|---|---:|---:|
| Desempenho | Tempo de resposta P95 | `< 500ms` |
| Carga | Throughput sustentado | `> 2000 req/s` |
| Estresse | Ponto de quebra | `> 15.000 usuários` |
| Escalabilidade | Eficiência horizontal | `> 80%` |
| Segurança | Rate limiting | `100 req/min/IP` |

## Instalação

```bash
pip install -r requirements.txt
```

## Executar a API local

```bash
uvicorn ecommerce.app:app --reload --app-dir src
```

A API fica disponível em `http://localhost:8000`.

## Executar os testes com pytest

```bash
PYTHONPATH=src pytest -v --benchmark-min-rounds=50
```

No Windows PowerShell:

```powershell
$env:PYTHONPATH="src"
pytest -v --benchmark-min-rounds=50
```

## Executar carga com Locust

```bash
locust -f locustfile.py --users 10000 --spawn-rate 500 --host http://localhost:8000
```

Abra `http://localhost:8089` para acompanhar as métricas em tempo real.

## Executar estresse/spike com Locust

```bash
locust -f stress_locust.py --users 15000 --spawn-rate 1000 --headless --host http://localhost:8000 --csv resultado_estresse
```

## Segurança

Análise estática:

```bash
bandit -r src -ll
```

Verificação de dependências:

```bash
safety check -r requirements.txt
```

## Relatório esperado

Os testes automatizados validam aprovação/reprovação das metas principais:

- P95 abaixo de 500ms.
- Throughput sustentado acima de 2000 req/s.
- Disponibilidade mínima de 99.9%.
- Ponto de quebra acima de 15.000 usuários.
- Eficiência horizontal acima de 80%.
- Rate limiting de 100 requisições por minuto por IP.
- Bloqueio de SQL injection e acesso administrativo sem token.
