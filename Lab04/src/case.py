# ─────────────────────────────────────────────────────────────────
# Exercício 1 – Caminhos Independentes
# ─────────────────────────────────────────────────────────────────
def verificar(n: int) -> str:
    if n > 0:
        if n % 2 == 0:
            return "Par positivo"
        else:
            return "Impar positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"


# ─────────────────────────────────────────────────────────────────
# Exercício 2 – Cobertura de Comandos e Ramos
# ─────────────────────────────────────────────────────────────────
def classificar(x: float) -> str:
    if x > 100:
        return "Alto"
    if x > 50:
        return "Medio"
    return "Baixo"


# ─────────────────────────────────────────────────────────────────
# Exercício 3 – Cobertura de Condição
# ─────────────────────────────────────────────────────────────────
def acesso(idade: int, membro: bool) -> str:
    if idade >= 18 and membro:
        return "Permitido"
    return "Negado"


# ─────────────────────────────────────────────────────────────────
# Exercício 4 – Teste de Ciclo
# ─────────────────────────────────────────────────────────────────
def somar_ate(n: int) -> int:
    soma = 0
    for i in range(n):
        soma += i
    return soma


# ─────────────────────────────────────────────────────────────────
# Exercício 5 – Teste de Ciclo Aninhado
# ─────────────────────────────────────────────────────────────────
def percorrer_matriz(m: int, n: int) -> int:
    contador = 0
    for i in range(m):
        for j in range(n):
            # print(f"Posicao ({i}, {j})")
            contador += 1
    return contador


# ─────────────────────────────────────────────────────────────────
# Exercício 6 – Teste Completo (Integrador)
# ─────────────────────────────────────────────────────────────────
def analisar(numeros: list) -> str:
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


# ─────────────────────────────────────────────────────────────────
# Exercício 7 – Fluxo de Dados
# ─────────────────────────────────────────────────────────────────
def desconto(preco: float, cliente_vip: bool) -> float:
    total = preco
    if cliente_vip:
        desconto_val = preco * 0.2
        total = preco - desconto_val
    if total < 50:
        total = 50
    return total