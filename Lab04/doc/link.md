```markdown
# Atividade 04 — Testes de Software

---

# Exercício 1 — Caminhos Independentes

## 1.1 Código analisado

```python
def verificar(n):

    if n > 0:

        if n % 2 == 0:
            return "Par positivo"

        else:
            return "Impar positivo"

    elif n < 0:
        return "Negativo"

    else:
        return "Zero"
```

---

## 1.2 Grafo de Fluxo de Controle (GFC)

```mermaid
flowchart TD
    N1(["Inicio verificar(n)"])
    N2{"n > 0"}
    N3{"n % 2 == 0"}
    N4["return 'Par positivo'"]
    N5["return 'Ímpar positivo'"]
    N6{"n < 0"}
    N7["return 'Negativo'"]
    N8["return 'Zero'"]
    END(["Fim"])

    N1 --> N2
    N2 -- Sim --> N3
    N2 -- Nao --> N6
    N3 -- Sim --> N4
    N3 -- Nao --> N5
    N6 -- Sim --> N7
    N6 -- Nao --> N8
    N4 --> END
    N5 --> END
    N7 --> END
    N8 --> END
```

---

## 1.3 Complexidade Ciclomática

Fórmula:

```
V(G) = E − N + 2
```

Onde:

```
E = 9 arestas
N = 8 nós
```

Logo:

```
V(G) = 9 − 8 + 2 = 3
```

Verificação alternativa:

```
nº de decisões + 1
3 + 1 = 4
```

Assim, existem **4 caminhos independentes**.

---

## 1.4 Caminhos Independentes

| Caminho | Sequência de Nós  | Condições     | Entrada |
| ------- | ----------------- | ------------- | ------- |
| C1      | N1→N2(F)→N6(F)→N8 | n = 0         | 0       |
| C2      | N1→N2(F)→N6(V)→N7 | n < 0         | -1      |
| C3      | N1→N2(V)→N3(V)→N4 | n > 0 e par   | 2       |
| C4      | N1→N2(V)→N3(F)→N5 | n > 0 e ímpar | 3       |

---

## 1.5 Casos de Teste

| CT  | Entrada | Saída Esperada   |
| --- | ------- | ---------------- |
| CT1 | 0       | "Zero"           |
| CT2 | -1      | "Negativo"       |
| CT3 | 2       | "Par positivo"   |
| CT4 | 3       | "Ímpar positivo" |

---

# Exercício 2 — Cobertura de Comandos e Ramos

## 2.1 Código analisado

```python
def classificar(x):

    if x > 100:
        return "Alto"

    if x > 50:
        return "Medio"

    return "Baixo"
```

---

## 2.2 Grafo de Fluxo de Controle

```mermaid
flowchart TD
    N1(["Inicio classificar(x)"])
    N2{"x > 100"}
    N3["return 'Alto'"]
    N4{"x > 50"}
    N5["return 'Medio'"]
    N6["return 'Baixo'"]
    END(["Fim"])

    N1 --> N2
    N2 -- Sim --> N3
    N2 -- Nao --> N4
    N4 -- Sim --> N5
    N4 -- Nao --> N6
    N3 --> END
    N5 --> END
    N6 --> END
```

---

## 2.3 Complexidade Ciclomática

```
V(G) = E − N + 2
V(G) = 6 − 5 + 2 = 3
```

ou

```
nº decisões + 1 = 2 + 1 = 3
```

---

## 2.4 Caminhos Independentes

```
C1: x > 100
C2: 50 < x ≤ 100
C3: x ≤ 50
```

---

## 2.5 Cobertura de Comandos (C0)

| CT  | x   | Retorno |
| --- | --- | ------- |
| CT1 | 150 | Alto    |
| CT2 | 75  | Medio   |
| CT3 | 30  | Baixo   |

---

## 2.6 Cobertura de Ramos (C1)

Os **mesmos 3 casos de teste** cobrem todos os ramos.

Logo:

```
C0 = C1 = 3 testes
```

---

# Exercício 3 — Cobertura de Condição

## 3.1 Código analisado

```python
def acesso(idade, membro):

    if idade >= 18 and membro:
        return "Permitido"

    return "Negado"
```

---

## 3.2 Grafo de Fluxo

```mermaid
flowchart TD
    N1(["Inicio acesso(idade, membro)"])
    N2{"idade >= 18 AND membro"}
    N3["return 'Permitido'"]
    N4["return 'Negado'"]

    N1 --> N2
    N2 -- Sim --> N3
    N2 -- Nao --> N4
```

---

## 3.3 Árvore de Condições

```mermaid
flowchart TD
    A{"idade >= 18"}
    A -- V --> B{"membro"}
    A -- F --> C["Negado"]
    B -- V --> D["Permitido"]
    B -- F --> E["Negado"]
```

---

## 3.4 Casos de Teste

| CT  | idade | membro | retorno   |
| --- | ----- | ------ | --------- |
| CT1 | 20    | True   | Permitido |
| CT2 | 20    | False  | Negado    |
| CT3 | 15    | True   | Negado    |
| CT4 | 15    | False  | Negado    |

---

# Exercício 4 — Teste de Ciclo

## 4.1 Código

```python
def somar_ate(n):

    soma = 0

    for i in range(n):
        soma += i

    return soma
```

---

## 4.2 Grafo de Fluxo

```mermaid
flowchart TD
    A(["Inicio"])
    B["soma = 0"]
    C{"for i in range(n)"}
    D["soma += i"]
    E["return soma"]

    A --> B
    B --> C
    C -- Sim --> D
    D --> C
    C -- Nao --> E
```

---

## 4.3 Casos de Teste

| CT  | n  | Iterações | Resultado |
| --- | -- | --------- | --------- |
| CT1 | 0  | 0         | 0         |
| CT2 | 1  | 1         | 0         |
| CT3 | 5  | 5         | 10        |
| CT4 | 10 | 10        | 45        |

Fórmula geral:

```
soma = n × (n−1) / 2
```

---

# Exercício 5 — Ciclos Aninhados

## 5.1 Código

```python
def percorrer_matriz(m, n):

    for i in range(m):
        for j in range(n):
            print(f"Posicao ({i}, {j})")
```

---

## 5.2 Grafo de Fluxo

```mermaid
flowchart TD
    A(["Inicio"])
    B{"for i"}
    C{"for j"}
    D["print(i,j)"]

    A --> B
    B -- Sim --> C
    B -- Nao --> Fim
    C -- Sim --> D
    D --> C
    C -- Nao --> B
```

---

## 5.3 Casos de Teste

| CT  | m | n | prints |
| --- | - | - | ------ |
| CT1 | 0 | 0 | 0      |
| CT2 | 1 | 0 | 0      |
| CT3 | 1 | 3 | 3      |
| CT4 | 3 | 3 | 9      |

Propriedade:

```
prints = m × n
```

---

# Exercício 6 — Teste Integrado

## 6.1 Código

```python
def analisar(numeros):

    total = 0

    for n in numeros:

        if n > 0 and n % 2 == 0:
            total += n

        elif n < 0:
            total -= 1

        else:
            continue

    if total > 10:
        return "Acima"

    return "Abaixo"
```

---

## 6.2 Grafo de Fluxo

```mermaid
flowchart TD
    A(["Inicio"])
    B["total = 0"]
    C{"for n"}
    D{"n > 0 AND par"}
    E["total += n"]
    F{"n < 0"}
    G["total -= 1"]
    H["continue"]
    I{"total > 10"}
    J["return 'Acima'"]
    K["return 'Abaixo'"]

    A --> B
    B --> C
    C -- Sim --> D
    C -- Nao --> I
    D -- Sim --> E
    D -- Nao --> F
    E --> C
    F -- Sim --> G
    F -- Nao --> H
    G --> C
    H --> C
    I -- Sim --> J
    I -- Nao --> K
```

---

## 6.3 Casos de Teste

| CT  | numeros    | total | retorno |
| --- | ---------- | ----- | ------- |
| CT1 | []         | 0     | Abaixo  |
| CT2 | [2]        | 2     | Abaixo  |
| CT3 | [2,4,6]    | 12    | Acima   |
| CT4 | [-1,-1,-1] | -3    | Abaixo  |
| CT5 | [1,3,5]    | 0     | Abaixo  |

---

# Exercício 7 — Fluxo de Dados

## 7.1 Código

```python
def desconto(preco, cliente_vip):

    total = preco

    if cliente_vip:

        desconto = preco * 0.2
        total = preco - desconto

    if total < 50:
        total = 50

    return total
```

---

## 7.2 Grafo de Fluxo

```mermaid
flowchart TD
    A(["Inicio"])
    B["total = preco"]
    C{"cliente_vip"}
    D["desconto = preco * 0.2"]
    E["total = preco - desconto"]
    F{"total < 50"}
    G["total = 50"]
    H["return total"]

    A --> B
    B --> C
    C -- Sim --> D
    D --> E
    E --> F
    C -- Nao --> F
    F -- Sim --> G
    F -- Nao --> H
    G --> H
```

---

## 7.3 Fluxo de Dados (Def-Use)

```mermaid
flowchart LR
    L2["def total"]
    L5["def total"]
    L7["def total"]
    L6{"uso total"}
    L8["return total"]

    L2 --> L6
    L2 --> L8
    L5 --> L6
    L5 --> L8
    L6 --> L7
    L7 --> L8
```

---

Link do arquivo Docs com as respostas: https://docs.google.com/document/d/1RHquYA6jhUPSlrOnjwelrdVjIzp9eO2I/edit?usp=sharing&ouid=103937993822110511313&rtpof=true&sd=true
