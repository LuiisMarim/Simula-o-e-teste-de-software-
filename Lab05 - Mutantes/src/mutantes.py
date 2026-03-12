# ============================================================
# Análise MANUAL de teste de mutação por substituição de operadores
# Cada mutante altera exatamente UM operador do código original.
# ============================================================

# ---------------------------------------------------------------
# MUTANTE 1  –  soma: substituir + por -
# Linha original:  return a + b
# Linha mutada:    return a - b
# ---------------------------------------------------------------
def soma_m1(a, b):
    return a - b          # + → -


# ---------------------------------------------------------------
# MUTANTE 2  –  soma: substituir + por *
# Linha original:  return a + b
# Linha mutada:    return a * b
# ---------------------------------------------------------------
def soma_m2(a, b):
    return a * b          # + → *


# ---------------------------------------------------------------
# MUTANTE 3  –  is_par: substituir == por !=
# Linha original:  return n % 2 == 0
# Linha mutada:    return n % 2 != 0
# ---------------------------------------------------------------
def is_par_m3(n):
    return n % 2 != 0     # == → !=


# ---------------------------------------------------------------
# MUTANTE 4  –  is_par: substituir % por /
# Linha original:  return n % 2 == 0
# Linha mutada:    return n / 2 == 0
# ---------------------------------------------------------------
def is_par_m4(n):
    return n / 2 == 0     # % → /


# ---------------------------------------------------------------
# MUTANTE 5  –  maior: substituir > por <
# Linha original:  if a > b:
# Linha mutada:    if a < b:
# ---------------------------------------------------------------
def maior_m5(a, b):
    if a < b:              # > → <
        return a
    else:
        return b


# ---------------------------------------------------------------
# MUTANTE 6  –  maior: substituir > por >=
# Linha original:  if a > b:
# Linha mutada:    if a >= b:
# ---------------------------------------------------------------
def maior_m6(a, b):
    if a >= b:             # > → >=
        return a
    else:
        return b


# ---------------------------------------------------------------
# MUTANTE 7  –  fatorial: substituir < por <=  (na validação)
# Linha original:  if n < 0:
# Linha mutada:    if n <= 0:
# ---------------------------------------------------------------
def fatorial_m7(n):
    if n <= 0:             # < → <=
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


# ---------------------------------------------------------------
# MUTANTE 8  –  fatorial: substituir * por +  (no acumulador)
# Linha original:  resultado = resultado * i
# Linha mutada:    resultado = resultado + i
# ---------------------------------------------------------------
def fatorial_m8(n):
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado + i   # * → +
    return resultado


# ---------------------------------------------------------------
# MUTANTE 9  –  fatorial: substituir + por - no range
# Linha original:  range(1, n + 1)
# Linha mutada:    range(1, n - 1)
# ---------------------------------------------------------------
def fatorial_m9(n):
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(1, n - 1):    # + → -
        resultado = resultado * i
    return resultado


# ---------------------------------------------------------------
# MUTANTE 10  –  classificar_nota: substituir >= por >  (primeira condição)
# Linha original:  if nota >= 7:
# Linha mutada:    if nota > 7:
# ---------------------------------------------------------------
def classificar_nota_m10(nota):
    if nota > 7:           # >= → >
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

