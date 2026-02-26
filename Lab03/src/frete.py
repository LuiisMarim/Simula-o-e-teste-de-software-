def calcular_frete(peso: float, destino: str, valor_pedido: float) -> float:
    if peso <= 0 or peso > 20:
        raise ValueError("Peso invalido")
        
    destinos_validos = ["mesma regiao", "outra regiao", "internacional"]
    if destino not in destinos_validos:
        raise ValueError("Destino invalido")
        
    if valor_pedido < 0:
        raise ValueError("Valor de pedido invalido")

    if valor_pedido > 200.00:
        return 0.0

    if peso <= 1.0:
        base = 10.0
    elif peso <= 5.0:
        base = 15.0
    else:
        base = 25.0

    if destino == "outra regiao":
        base *= 1.5
    elif destino == "internacional":
        base *= 2.0

    return float(base)