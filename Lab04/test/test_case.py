import pytest
import sys
sys.path.insert(0, '/workspaces/Simula-o-e-teste-de-software-/Lab04/src')
from case import (
    verificar,
    classificar,
    acesso,
    somar_ate,
    percorrer_matriz,
    analisar,
    desconto,
)


# ═══════════════════════════════════════════════════════════════════
# Exercício 1 – Caminhos Independentes
# ═══════════════════════════════════════════════════════════════════
def test_verificar_caminho_c1_retorna_zero_quando_n_igual_a_zero():
    """C1: N1→N2(F)→N6(F)→N8  |  n=0  |  resultado: 'Zero'"""
    assert verificar(0) == "Zero"


def test_verificar_caminho_c2_retorna_negativo_quando_n_menor_que_zero():
    """C2: N1→N2(F)→N6(V)→N7  |  n=-1  |  resultado: 'Negativo'"""
    assert verificar(-1) == "Negativo"


def test_verificar_caminho_c3_retorna_par_positivo_quando_n_par_e_positivo():
    """C3: N1→N2(V)→N3(V)→N4  |  n=2  |  resultado: 'Par positivo'"""
    assert verificar(2) == "Par positivo"


def test_verificar_caminho_c4_retorna_impar_positivo_quando_n_impar_e_positivo():
    """C4: N1→N2(V)→N3(F)→N5  |  n=3  |  resultado: 'Impar positivo'"""
    assert verificar(3) == "Impar positivo"


# Casos adicionais para robustez
def test_verificar_valor_negativo_grande_retorna_negativo():
    assert verificar(-100) == "Negativo"


def test_verificar_valor_par_positivo_grande_retorna_par_positivo():
    assert verificar(100) == "Par positivo"


# ═══════════════════════════════════════════════════════════════════
# Exercício 2 – Cobertura de Comandos (C0) e Ramos (C1)
# ═══════════════════════════════════════════════════════════════════
# ── Cobertura de Comandos (C0) ──────────────────────────────
def test_classificar_c0_cobre_return_alto_quando_x_maior_que_100():
    """C0/C1 – C1: N1→N2(V)→N3  |  x=150  |  resultado: 'Alto'"""
    assert classificar(150) == "Alto"


def test_classificar_c0_cobre_return_medio_quando_x_entre_50_e_100():
    """C0/C1 – C2: N1→N2(F)→N4(V)→N5  |  x=75  |  resultado: 'Medio'"""
    assert classificar(75) == "Medio"


def test_classificar_c0_cobre_return_baixo_quando_x_menor_ou_igual_a_50():
    """C0/C1 – C3: N1→N2(F)→N4(F)→N6  |  x=30  |  resultado: 'Baixo'"""
    assert classificar(30) == "Baixo"


# ── Cobertura de Ramos (C1) – fronteiras ───────────────────
def test_classificar_c1_fronteira_exatamente_100_retorna_medio():
    """Valor de fronteira: x=100 → 'Medio' (não entra em x>100)"""
    assert classificar(100) == "Medio"


def test_classificar_c1_fronteira_exatamente_50_retorna_baixo():
    """Valor de fronteira: x=50 → 'Baixo' (não entra em x>50)"""
    assert classificar(50) == "Baixo"


def test_classificar_c1_fronteira_101_retorna_alto():
    """Valor de fronteira: x=101 → 'Alto'"""
    assert classificar(101) == "Alto"


# ═══════════════════════════════════════════════════════════════════
# Exercício 3 – Cobertura de Condição (CC)
# ═══════════════════════════════════════════════════════════════════
# ── Cobertura de Condição Múltipla (CMC) – 4 combinações ───
def test_acesso_cc_cmc_idade_maior_e_membro_verdadeiro_permite_acesso():
    """CC/CMC – CT1: idade>=18=V, membro=V  →  'Permitido'"""
    assert acesso(20, True) == "Permitido"


def test_acesso_cc_cmc_idade_maior_e_membro_falso_nega_acesso():
    """CC/CMC – CT2: idade>=18=V, membro=F  →  'Negado'"""
    assert acesso(20, False) == "Negado"


def test_acesso_cc_cmc_idade_menor_e_membro_verdadeiro_nega_acesso():
    """CC/CMC – CT3: idade>=18=F, membro=V  →  'Negado'"""
    assert acesso(15, True) == "Negado"


def test_acesso_cc_cmc_idade_menor_e_membro_falso_nega_acesso():
    """CC/CMC – CT4: idade>=18=F, membro=F  →  'Negado'"""
    assert acesso(15, False) == "Negado"


# ── Fronteiras de idade ─────────────────────────────────────
def test_acesso_c1_fronteira_exatamente_18_com_membro_permite_acesso():
    """Fronteira: idade=18 (mínimo permitido) e membro=True → 'Permitido'"""
    assert acesso(18, True) == "Permitido"


def test_acesso_c1_fronteira_17_com_membro_nega_acesso():
    """Fronteira: idade=17 (abaixo do limite) e membro=True → 'Negado'"""
    assert acesso(17, True) == "Negado"


# ═══════════════════════════════════════════════════════════════════
# Exercício 4 – Teste de Ciclo (Laço Simples)
# ═══════════════════════════════════════════════════════════════════
def test_somar_ate_ciclo_ignorado_com_zero_iteracoes_retorna_zero():
    """Laço ignorado (0 iterações): n=0 → soma=0"""
    assert somar_ate(0) == 0


def test_somar_ate_ciclo_com_uma_iteracao_retorna_zero():
    """1 iteração: n=1, i=0 → soma=0"""
    assert somar_ate(1) == 0


def test_somar_ate_ciclo_com_duas_iteracoes_retorna_um():
    """2 iterações: n=2, soma=0+1=1"""
    assert somar_ate(2) == 1


def test_somar_ate_ciclo_com_cinco_iteracoes_retorna_dez():
    """Múltiplas iterações: n=5, soma=0+1+2+3+4=10"""
    assert somar_ate(5) == 10


def test_somar_ate_ciclo_com_dez_iteracoes_retorna_quarenta_e_cinco():
    """Múltiplas iterações: n=10, soma=0+1+...+9=45"""
    assert somar_ate(10) == 45


@pytest.mark.parametrize("n,esperado", [
    (3, 3),   # 0+1+2 = 3
    (4, 6),   # 0+1+2+3 = 6
    (6, 15),  # 0+1+2+3+4+5 = 15
    (7, 21),  # 0+1+2+3+4+5+6 = 21
])
def test_somar_ate_formula_geral_para_valores_variados(n, esperado):
    """Verifica a fórmula n*(n-1)//2 para vários valores"""
    assert somar_ate(n) == esperado


# ═══════════════════════════════════════════════════════════════════
# Exercício 5 – Teste de Ciclo Aninhado
# ═══════════════════════════════════════════════════════════════════
def test_percorrer_matriz_ambos_lacos_ignorados_quando_m_e_n_sao_zero():
    """CT1: m=0, n=0 → 0 execuções (ambos ignorados)"""
    assert percorrer_matriz(0, 0) == 0


def test_percorrer_matriz_laco_externo_ignorado_quando_m_zero_independente_de_n():
    """CT1b: m=0, n=5 → 0 execuções (laço externo ignorado)"""
    assert percorrer_matriz(0, 5) == 0


def test_percorrer_matriz_laco_interno_ignorado_quando_n_zero():
    """CT2: m=1, n=0 → 0 execuções (laço j ignorado)"""
    assert percorrer_matriz(1, 0) == 0


def test_percorrer_matriz_laco_externo_uma_vez_interno_varias_vezes():
    """CT3: m=1, n=3 → 3 execuções (i executa 1x, j executa 3x)"""
    assert percorrer_matriz(1, 3) == 3


def test_percorrer_matriz_ambos_lacos_varias_vezes():
    """CT4: m=3, n=3 → 9 execuções (ambos executam múltiplas vezes)"""
    assert percorrer_matriz(3, 3) == 9


def test_percorrer_matriz_laco_externo_varias_vezes_interno_uma_vez():
    """CT5: m=4, n=1 → 4 execuções (i executa 4x, j executa 1x cada)"""
    assert percorrer_matriz(4, 1) == 4


@pytest.mark.parametrize("m,n", [(2, 5), (3, 4), (10, 10)])
def test_percorrer_matriz_contagem_igual_a_produto_m_por_n(m, n):
    """Propriedade geral: resultado = m * n"""
    assert percorrer_matriz(m, n) == m * n


# ═══════════════════════════════════════════════════════════════════
# Exercício 6 – Teste Completo (Integrador)
# ═══════════════════════════════════════════════════════════════════
# ── Comportamento do laço (0, 1 e várias iterações) ────────
def test_analisar_ciclo_ignorado_lista_vazia_retorna_abaixo():
    """0 iterações: lista vazia → total=0 → 'Abaixo'"""
    assert analisar([]) == "Abaixo"


def test_analisar_ciclo_uma_iteracao_par_positivo_retorna_abaixo():
    """1 iteração: n=2 (par positivo) → total=2 ≤ 10 → 'Abaixo'"""
    assert analisar([2]) == "Abaixo"


def test_analisar_ciclo_varias_iteracoes_pares_positivos_retorna_acima():
    """Várias iterações: [2,4,6] → total=12 > 10 → 'Acima'"""
    assert analisar([2, 4, 6]) == "Acima"


# ── Cobertura de Comandos e Ramos (C0/C1) ──────────────────
def test_analisar_c0_c1_n_negativo_decrementa_total():
    """C0/C1 – ramo elif n<0: [-1,-1,...] → total<0 → 'Abaixo'"""
    assert analisar([-1, -1, -1]) == "Abaixo"


def test_analisar_c0_c1_n_impar_positivo_executa_continue():
    """C0/C1 – ramo else (continue): [1,3,5] → total=0 → 'Abaixo'"""
    assert analisar([1, 3, 5]) == "Abaixo"


def test_analisar_c1_total_exatamente_10_retorna_abaixo():
    """Fronteira: [2,4,4] → total=10 (não > 10) → 'Abaixo'"""
    assert analisar([2, 4, 4]) == "Abaixo"


def test_analisar_c1_total_exatamente_11_retorna_acima():
    """Fronteira: [2,4,6] → total=12 > 10 → 'Acima'"""
    assert analisar([2, 4, 6]) == "Acima"


# ── Cobertura de Condição (CC) para n>0 and n%2==0 ─────────
def test_analisar_cc_n_positivo_e_par_soma_ao_total():
    """CC – CT-A: n>0=V, n%2==0=V → total += n  (n=4)"""
    assert analisar([4]) == "Abaixo"


def test_analisar_cc_n_positivo_e_impar_nao_soma():
    """CC – CT-B: n>0=V, n%2==0=F → vai para elif (n=3 → n>=0 → continue)"""
    assert analisar([3]) == "Abaixo"


def test_analisar_cc_n_negativo_decrementa():
    """CC – CT-C: n>0=F → elif n<0=V → total -= 1  (n=-5)"""
    assert analisar([-5]) == "Abaixo"


def test_analisar_cc_n_zero_executa_continue():
    """CC – CT-D: n=0 → n>0=F, n<0=F → continue"""
    assert analisar([0]) == "Abaixo"


# ── Combinações complexas ────────────────────────────────────
def test_analisar_mix_de_pares_impares_e_negativos_retorna_abaixo():
    """Mix: [2, 3, -1] → total = 2-1 = 1 → 'Abaixo'"""
    assert analisar([2, 3, -1]) == "Abaixo"


def test_analisar_mix_que_supera_10_retorna_acima():
    """Mix: [2, 4, 6, -1] → total = 2+4+6-1 = 11 > 10 → 'Acima'"""
    assert analisar([2, 4, 6, -1]) == "Acima"


# ═══════════════════════════════════════════════════════════════════
# Exercício 7 – Fluxo de Dados (All-Defs / All-Uses)
# ═══════════════════════════════════════════════════════════════════
# ── All-Defs: cada definição alcança ao menos um uso ────────
def test_desconto_all_defs_cliente_vip_preco_alto_aplica_desconto():
    """
    All-Defs CT1: preco=100, vip=True
    def(preco)→uso(L2,L4,L5), def(total,L5)→uso(L6), def(desconto)→uso(L5)
    total = 100 - 20 = 80 ≥ 50 → retorna 80.0
    Cobre P1, P2, P3, P4, P8, P10, P12.
    """
    assert desconto(100.0, True) == 80.0


def test_desconto_all_defs_cliente_normal_preco_alto_sem_desconto():
    """
    All-Defs CT2: preco=100, vip=False
    def(total,L2)→uso(L6): total=100 ≥ 50 → retorna 100.0
    Cobre P1, P4, P5, P7.
    """
    assert desconto(100.0, False) == 100.0


# ── All-Uses: cobrir todos os pares def-uso ─────────────────
def test_desconto_all_uses_vip_preco_abaixo_do_minimo_aplica_preco_minimo():
    """
    All-Uses CT3: preco=30, vip=True
    total = 30 - 6 = 24 < 50 → total = 50
    Cobre P2, P3, P9, P11, P12.
    """
    assert desconto(30.0, True) == 50.0


def test_desconto_all_uses_normal_preco_abaixo_do_minimo_aplica_preco_minimo():
    """
    All-Uses CT4: preco=30, vip=False
    total = 30 < 50 → total = 50
    Cobre P5 (→L6=V), P6, P11.
    """
    assert desconto(30.0, False) == 50.0


def test_desconto_all_uses_vip_preco_na_fronteira_desconto_cai_abaixo_do_minimo():
    """
    Fronteira P9: preco=62, vip=True
    total = 62 - 12.4 = 49.6 < 50 → total = 50
    Par def(total,L5)→uso(total,L7) explicitamente coberto.
    """
    assert desconto(62.0, True) == 50.0


def test_desconto_all_uses_vip_preco_na_fronteira_desconto_nao_cai_abaixo():
    """
    Fronteira P10: preco=63, vip=True
    total = 63 - 12.6 = 50.4 ≥ 50 → retorna 50.4
    Par def(total,L5)→uso(total,L8) coberto.
    """
    assert desconto(63.0, True) == 50.4


def test_desconto_preco_exatamente_50_com_vip_fica_em_40_e_sobe_para_50():
    """preco=50, vip=True → total=40 < 50 → retorna 50.0"""
    assert desconto(50.0, True) == 50.0


def test_desconto_preco_zero_retorna_minimo():
    """preco=0, vip=False → total=0 < 50 → retorna 50.0"""
    assert desconto(0.0, False) == 50.0


# ── Verificação da cobertura de ramos C1 ────────────────────
def test_desconto_c1_ramo_vip_verdadeiro_e_total_maior_igual_50():
    """C1 – ramo if cliente_vip=V e if total<50=F"""
    assert desconto(200.0, True) == 160.0


def test_desconto_c1_ramo_vip_falso_e_total_maior_igual_50():
    """C1 – ramo if cliente_vip=F e if total<50=F"""
    assert desconto(200.0, False) == 200.0


# ═══════════════════════════════════════════════════════════════════
# Testes agrupados com classes (opcional, mas útil para organização)
# ═══════════════════════════════════════════════════════════════════

class TestDescontoAvancado:
    """Versão com classe para agrupar testes relacionados (opcional)"""
    
    def test_preco_negativo_retorna_minimo(self):
        assert desconto(-10.0, False) == 50.0
    
    def test_preco_muito_alto_com_vip(self):
        assert desconto(1000.0, True) == 800.0
    
    @pytest.mark.parametrize("preco,esperado", [
        (49.99, 50.0),
        (50.0, 50.0),
        (50.01, 50.01),
    ])
    def test_fronteiras_preco_minimo(self, preco, esperado):
        assert desconto(preco, False) == esperado