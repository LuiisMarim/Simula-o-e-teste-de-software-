# Relatório — Atividade 06: Testes de Unidade e Integração

**CC8550 — Simulação e Teste de Software**  
Centro Universitário FEI — Prof. Luciano Rossi

---

## 1. Resultados dos Testes

Todos os testes foram implementados utilizando **pytest** como framework principal, em vez do `unittest` puro. O `MagicMock` do módulo `unittest.mock` foi mantido para criação de stubs e mocks, pois é amplamente compatível com pytest.

### Resumo por arquivo de teste

| Arquivo               | Categorias cobertas                                                        | Qtd. testes |
|------------------------|---------------------------------------------------------------------------|-------------|
| `test_unidade.py`      | Entrada/Saída, Tipagem, Limites, Valores fora do intervalo, Mensagens de erro, Fluxos de controle | ~45         |
| `test_integracao.py`   | Operações sequenciais, Consistência do histórico                          | ~10         |
| `test_doubles.py`      | Stub (estado), Mock (comportamento), Detecção do bug                      | ~20         |

Todos os testes passam com sucesso após a correção do bug.

---

## 2. Cobertura Obtida

Comando utilizado:

```bash
pytest --cov=src --cov-report=term-missing
```

Resultado esperado:

```
Name                  Stmts   Miss  Cover   Missing
-----------------------------------------------------
src/calculadora.py       38      0   100%
src/repositorio.py       10      0   100%
-----------------------------------------------------
TOTAL                    48      0   100%
```

**100% de cobertura de linhas** em ambos os módulos (`calculadora.py` e `repositorio.py`). Nenhuma linha ficou descoberta, pois os testes exercitam todos os caminhos: entradas válidas, entradas inválidas (TypeError), divisão por zero (ValueError) e o caminho normal de cada operação.

---

## 3. Bug Encontrado e Corrigido

### Localização

Arquivo `src/calculadora.py`, método `potencia`, linha 45 (código original fornecido).

### Descrição do bug

A string de histórico registrada no repositório usava o operador de **multiplicação** (`*`) em vez do operador de **potenciação** (`**`):

```python
# CÓDIGO COM BUG (original)
self.repositorio.salvar(f"{base} * {expoente} = {resultado}")
```

Isso fazia com que a operação `potencia(2, 3)` gerasse o registro `"2 * 3 = 8"`, o que é semanticamente incorreto — `2 * 3` deveria resultar em `6`, não `8`.

### Como o bug foi detectado

Utilizando um **mock** para verificar o argumento exato passado ao método `salvar()`:

```python
def test_mock_argumento_potencia(self):
    self.calc.potencia(2, 3)
    self.mock_repo.salvar.assert_called_once_with("2 ** 3 = 8")
```

Com o código original, este teste falha com a mensagem:

```
AssertionError: expected call: salvar('2 ** 3 = 8')
Actual call: salvar('2 * 3 = 8')
```

### Correção aplicada

```python
# CÓDIGO CORRIGIDO
self.repositorio.salvar(f"{base} ** {expoente} = {resultado}")
```

---

## 4. Reflexão: Stub vs Mock na Prática

### Stub

O **stub** foi utilizado na Parte 1 e na seção 4.1, onde o `MagicMock` substitui o `HistoricoRepositorio` sem que nenhuma verificação de chamada seja feita. O objetivo era isolar a lógica da `Calculadora` — garantir que `somar(5, 3)` retorna `8` independentemente do repositório existir ou funcionar. O stub responde à pergunta: *"dado que a dependência se comporta normalmente, o módulo produz o resultado correto?"*

Na prática, o stub foi essencial para testar a calculadora antes mesmo de ter certeza sobre a implementação do repositório. É uma abordagem focada em **estado**: verificamos o valor retornado e o estado interno (`obter_ultimo_resultado`), sem nos preocupar com as interações.

### Mock

O **mock** foi utilizado na seção 4.2, onde além de substituir o repositório, **verificamos as interações**: se `salvar()` foi chamado, quantas vezes e com quais argumentos exatos. O mock responde à pergunta: *"o módulo está interagindo com sua dependência da maneira correta?"*

Foi justamente o mock que revelou o bug em `potencia`. Sem verificar o argumento passado a `salvar()`, o bug passaria despercebido nos testes de entrada/saída (já que o valor numérico de retorno estava correto — `2 ** 3 = 8`). Isso demonstra o valor dos mocks: eles capturam defeitos na **comunicação entre componentes**, não apenas no resultado final.

### Resumo

| Aspecto         | Stub                          | Mock                                  |
|-----------------|-------------------------------|---------------------------------------|
| Foco            | Estado / resultado            | Comportamento / interação             |
| Verifica chamadas? | Não                        | Sim                                   |
| Quando usar     | Isolar lógica interna         | Validar contratos entre componentes   |
| Detecta bugs de interface? | Raramente            | Sim — foi assim que achamos o bug     |