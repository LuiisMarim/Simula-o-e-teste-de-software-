# programa.py

from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore
def soma(a, b):
    args = [a, b]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_soma__mutmut_orig, x_soma__mutmut_mutants, args, kwargs, None)
def x_soma__mutmut_orig(a, b):
    """Retorna a soma de dois números."""
    return a + b
def x_soma__mutmut_1(a, b):
    """Retorna a soma de dois números."""
    return a - b

x_soma__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_soma__mutmut_1': x_soma__mutmut_1
}
x_soma__mutmut_orig.__name__ = 'x_soma'


def is_par(n):
    args = [n]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_par__mutmut_orig, x_is_par__mutmut_mutants, args, kwargs, None)


def x_is_par__mutmut_orig(n):
    """Retorna True se n for par, False caso contrário."""
    return n % 2 == 0


def x_is_par__mutmut_1(n):
    """Retorna True se n for par, False caso contrário."""
    return n / 2 == 0


def x_is_par__mutmut_2(n):
    """Retorna True se n for par, False caso contrário."""
    return n % 3 == 0


def x_is_par__mutmut_3(n):
    """Retorna True se n for par, False caso contrário."""
    return n % 2 != 0


def x_is_par__mutmut_4(n):
    """Retorna True se n for par, False caso contrário."""
    return n % 2 == 1

x_is_par__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_is_par__mutmut_1': x_is_par__mutmut_1, 
    'x_is_par__mutmut_2': x_is_par__mutmut_2, 
    'x_is_par__mutmut_3': x_is_par__mutmut_3, 
    'x_is_par__mutmut_4': x_is_par__mutmut_4
}
x_is_par__mutmut_orig.__name__ = 'x_is_par'


def maior(a, b):
    args = [a, b]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_maior__mutmut_orig, x_maior__mutmut_mutants, args, kwargs, None)


def x_maior__mutmut_orig(a, b):
    """Retorna o maior entre dois números."""
    if a > b:
        return a
    else:
        return b


def x_maior__mutmut_1(a, b):
    """Retorna o maior entre dois números."""
    if a >= b:
        return a
    else:
        return b

x_maior__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_maior__mutmut_1': x_maior__mutmut_1
}
x_maior__mutmut_orig.__name__ = 'x_maior'


def fatorial(n):
    args = [n]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_fatorial__mutmut_orig, x_fatorial__mutmut_mutants, args, kwargs, None)


def x_fatorial__mutmut_orig(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_1(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n <= 0:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_2(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 1:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_3(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError(None)
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_4(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("XXn deve ser >= 0XX")
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_5(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("N DEVE SER >= 0")
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_6(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = None
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_7(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = 2
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_8(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(None, n + 1):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_9(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(1, None):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_10(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(n + 1):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_11(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(1, ):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_12(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(2, n + 1):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_13(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(1, n - 1):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_14(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(1, n + 2):
        resultado = resultado * i
    return resultado


def x_fatorial__mutmut_15(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(1, n + 1):
        resultado = None
    return resultado


def x_fatorial__mutmut_16(n):
    """Retorna o fatorial de n (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado / i
    return resultado

x_fatorial__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_fatorial__mutmut_1': x_fatorial__mutmut_1, 
    'x_fatorial__mutmut_2': x_fatorial__mutmut_2, 
    'x_fatorial__mutmut_3': x_fatorial__mutmut_3, 
    'x_fatorial__mutmut_4': x_fatorial__mutmut_4, 
    'x_fatorial__mutmut_5': x_fatorial__mutmut_5, 
    'x_fatorial__mutmut_6': x_fatorial__mutmut_6, 
    'x_fatorial__mutmut_7': x_fatorial__mutmut_7, 
    'x_fatorial__mutmut_8': x_fatorial__mutmut_8, 
    'x_fatorial__mutmut_9': x_fatorial__mutmut_9, 
    'x_fatorial__mutmut_10': x_fatorial__mutmut_10, 
    'x_fatorial__mutmut_11': x_fatorial__mutmut_11, 
    'x_fatorial__mutmut_12': x_fatorial__mutmut_12, 
    'x_fatorial__mutmut_13': x_fatorial__mutmut_13, 
    'x_fatorial__mutmut_14': x_fatorial__mutmut_14, 
    'x_fatorial__mutmut_15': x_fatorial__mutmut_15, 
    'x_fatorial__mutmut_16': x_fatorial__mutmut_16
}
x_fatorial__mutmut_orig.__name__ = 'x_fatorial'


def classificar_nota(nota):
    args = [nota]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_classificar_nota__mutmut_orig, x_classificar_nota__mutmut_mutants, args, kwargs, None)


def x_classificar_nota__mutmut_orig(nota):
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


def x_classificar_nota__mutmut_1(nota):
    """Classifica uma nota de 0 a 10.
    >= 7: 'Aprovado'
    >= 5 e < 7: 'Recuperação'
    < 5: 'Reprovado'
    """
    if nota > 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def x_classificar_nota__mutmut_2(nota):
    """Classifica uma nota de 0 a 10.
    >= 7: 'Aprovado'
    >= 5 e < 7: 'Recuperação'
    < 5: 'Reprovado'
    """
    if nota >= 8:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def x_classificar_nota__mutmut_3(nota):
    """Classifica uma nota de 0 a 10.
    >= 7: 'Aprovado'
    >= 5 e < 7: 'Recuperação'
    < 5: 'Reprovado'
    """
    if nota >= 7:
        return "XXAprovadoXX"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def x_classificar_nota__mutmut_4(nota):
    """Classifica uma nota de 0 a 10.
    >= 7: 'Aprovado'
    >= 5 e < 7: 'Recuperação'
    < 5: 'Reprovado'
    """
    if nota >= 7:
        return "aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def x_classificar_nota__mutmut_5(nota):
    """Classifica uma nota de 0 a 10.
    >= 7: 'Aprovado'
    >= 5 e < 7: 'Recuperação'
    < 5: 'Reprovado'
    """
    if nota >= 7:
        return "APROVADO"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def x_classificar_nota__mutmut_6(nota):
    """Classifica uma nota de 0 a 10.
    >= 7: 'Aprovado'
    >= 5 e < 7: 'Recuperação'
    < 5: 'Reprovado'
    """
    if nota >= 7:
        return "Aprovado"
    elif nota > 5:
        return "Recuperação"
    else:
        return "Reprovado"


def x_classificar_nota__mutmut_7(nota):
    """Classifica uma nota de 0 a 10.
    >= 7: 'Aprovado'
    >= 5 e < 7: 'Recuperação'
    < 5: 'Reprovado'
    """
    if nota >= 7:
        return "Aprovado"
    elif nota >= 6:
        return "Recuperação"
    else:
        return "Reprovado"


def x_classificar_nota__mutmut_8(nota):
    """Classifica uma nota de 0 a 10.
    >= 7: 'Aprovado'
    >= 5 e < 7: 'Recuperação'
    < 5: 'Reprovado'
    """
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "XXRecuperaçãoXX"
    else:
        return "Reprovado"


def x_classificar_nota__mutmut_9(nota):
    """Classifica uma nota de 0 a 10.
    >= 7: 'Aprovado'
    >= 5 e < 7: 'Recuperação'
    < 5: 'Reprovado'
    """
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "recuperação"
    else:
        return "Reprovado"


def x_classificar_nota__mutmut_10(nota):
    """Classifica uma nota de 0 a 10.
    >= 7: 'Aprovado'
    >= 5 e < 7: 'Recuperação'
    < 5: 'Reprovado'
    """
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "RECUPERAÇÃO"
    else:
        return "Reprovado"


def x_classificar_nota__mutmut_11(nota):
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
        return "XXReprovadoXX"


def x_classificar_nota__mutmut_12(nota):
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
        return "reprovado"


def x_classificar_nota__mutmut_13(nota):
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
        return "REPROVADO"

x_classificar_nota__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_classificar_nota__mutmut_1': x_classificar_nota__mutmut_1, 
    'x_classificar_nota__mutmut_2': x_classificar_nota__mutmut_2, 
    'x_classificar_nota__mutmut_3': x_classificar_nota__mutmut_3, 
    'x_classificar_nota__mutmut_4': x_classificar_nota__mutmut_4, 
    'x_classificar_nota__mutmut_5': x_classificar_nota__mutmut_5, 
    'x_classificar_nota__mutmut_6': x_classificar_nota__mutmut_6, 
    'x_classificar_nota__mutmut_7': x_classificar_nota__mutmut_7, 
    'x_classificar_nota__mutmut_8': x_classificar_nota__mutmut_8, 
    'x_classificar_nota__mutmut_9': x_classificar_nota__mutmut_9, 
    'x_classificar_nota__mutmut_10': x_classificar_nota__mutmut_10, 
    'x_classificar_nota__mutmut_11': x_classificar_nota__mutmut_11, 
    'x_classificar_nota__mutmut_12': x_classificar_nota__mutmut_12, 
    'x_classificar_nota__mutmut_13': x_classificar_nota__mutmut_13
}
x_classificar_nota__mutmut_orig.__name__ = 'x_classificar_nota'