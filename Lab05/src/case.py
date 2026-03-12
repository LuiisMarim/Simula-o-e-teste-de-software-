# programa.py

def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b


def is_par(n):
    """Retorna True se n for par, False caso contrário."""
    return n % 2 == 0


def maior(a, b):
    """Retorna o maior entre dois números."""
    if a > b:
        return a
    else:
        return b


def fatorial(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


def classificar_nota(nota):
    """Classifica uma nota de 0 a 10.
    >= 7: 'Aprovado'
    >= 5 e < 7: 'Recuperação'
    < 5: 'Reprovado'
    """
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"