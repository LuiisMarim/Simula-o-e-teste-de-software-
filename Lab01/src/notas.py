def validar_nota (nota):
    return 0 <= nota <= 10


def calcular_media (notas):
    if len(notas) == 0:
        raise ValueError("Lista vazia")
    return sum(notas)/ len(notas)

def obter_situacao(media):
    if media > 10:
        raise ValueError("Média inválida")
    return 'Reprovado' if media < 5 else 'Aprovado'

def calcular_estatisticas(notas):
    if not notas:
        return {
            'quantidade': 0,
            'media': 0,
            'maior': None,
            'menor': None
        }
    return {
        'quantidade': len(notas),
        'media': calcular_media(notas),
        'maior': max(notas),
        'menor': min(notas),
        'aprovados': sum(1 for nota in notas if nota > 5),
        'reprovados': sum(1 for nota in notas if nota < 5)
    }

def normalizar_notas(notas, max):
    if max <= 0:
        raise ValueError('O valor máximo deve ser maior que zero')

    return [(nota / max) * 10 for nota in notas]