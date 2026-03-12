# Análise Automatizada com Mutmut

## Estrutura de Arquivos

```
projeto/
├── programa.py
├── test_programa.py
└── setup.cfg          (opcional)
```

## 1. Instalação

```bash
pip install mutmut pytest
```

## 2. Configuração (opcional – setup.cfg)

```ini
[mutmut]
paths_to_mutate=programa.py
tests_dir=.
runner=python -m pytest -x --tb=short
```

## 3. Executar o Mutmut

```bash
mutmut run --paths-to-mutate=case.py
```

## 4. Ver Resultados

```bash
# Resumo geral
mutmut results

# Ver detalhes de um mutante específico (ex: mutante 1)
mutmut show 1

# Exportar relatório HTML
mutmut html
```

## 5. Interpretação dos Resultados

O mutmut classifica cada mutante como:

| Status     | Significado                        |
|------------|------------------------------------|
| killed     | Teste detectou a mutação (bom!)    |
| survived   | Nenhum teste detectou (ruim!)      |
| timeout    | Mutação gerou loop infinito        |
| suspicious | Comportamento inesperado           |

## 6. Comparação Esperada: Manual vs. Automatizada

| Aspecto                    | Manual        | Mutmut (automatizado)   |
|----------------------------|---------------|-------------------------|
| Nº de mutantes criados     | 10            | ~15-25 (varia)          |
| Tipos de mutação           | Só operadores | Operadores + literais + remoção de linhas |
| Mutantes mortos (estimado) | 8 / 10        | ~80-85% dos gerados     |
| Mutantes sobreviventes     | 2 / 10        | Alguns a mais           |
| Esforço                    | Alto (manual) | Baixo (automático)      |
| Precisão da análise        | Controlada    | Pode incluir equivalentes |

### Mutantes que provavelmente sobrevivem em ambas as abordagens:

1. **`>` → `>=` em `maior()`** — sem teste com valores iguais
2. **`>=` → `>` em `classificar_nota()`** — sem teste no valor limite 7

### Como melhorar o Mutation Score:

Adicionar ao `test_programa.py`:

```python
def test_maior_iguais():
    assert maior(5, 5) == 5

def test_classificar_nota_limite_7():
    assert classificar_nota(7) == "Aprovado"

def test_classificar_nota_recuperacao():
    assert classificar_nota(5) == "Recuperação"

def test_classificar_nota_reprovado():
    assert classificar_nota(4) == "Reprovado"
```

Com esses testes adicionais, o Mutation Score deve subir para próximo de 100%.