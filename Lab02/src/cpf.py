def limpar_cpf(cpf: str) -> str:
    return ''.join(filter(str.isdigit, cpf))

def formatar_cpf(cpf: str) -> str:
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11:
        raise ValueError("CPF deve conter 11 digitos")

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def validar_cpf(cpf: str) -> bool:
    cpf = limpar_cpf(cpf)

    if any(letra.isalpha() for letra in cpf):
        raise ValueError("CPF deve conter apenas digitos")

    if len(cpf) != 11:
        return False


    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = (soma * 10 % 11) % 10

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = (soma * 10 % 11) % 10

    return cpf[9] == str(primeiro_digito) and cpf[10] == str(segundo_digito)        
