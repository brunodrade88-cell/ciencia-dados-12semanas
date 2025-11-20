"""
Módulo de Indicadores Financeiros

Este módulo contém funções para calcular indicadores
financeiros de empresas.

Autor: Bruno Andrade
Data: 13/11/2025
"""


def calcular_margem_liquida(receita, lucro):
    """
    Calcula margem líquida em percentual.

    Args:
        receita (float): Receita líquida
        lucro (float): Lucro líquido

    Returns:
        float: Margem líquida (%)
    """
    if receita == 0:
        return 0
    return (lucro / receita) * 100


def calcular_roe(lucro_liquido, patrimonio_liquido):
    """
    Calcula ROE (Return on Equity).

    Args:
        lucro_liquido (float): Lucro líquido do período
        patrimonio_liquido (float): Patrimônio líquido

    Returns:
        float: ROE em percentual
    """
    if patrimonio_liquido == 0:
        return 0
    return (lucro_liquido / patrimonio_liquido) * 100


def calcular_liquidez_corrente(ativo_circulante, passivo_circulante):
    """
    Calcula liquidez corrente.

    Args:
        ativo_circulante (float): Ativo circulante
        passivo_circulante (float): Passivo circulante

    Returns:
        float: Índice de liquidez corrente
    """
    if passivo_circulante == 0:
        return float('inf')
    return ativo_circulante / passivo_circulante


def calcular_roa(lucro_liquido, ativo_total):
    """
    Calcula ROA (Return on Assets).

    Args:
        lucro_liquido (float): Lucro líquido
        ativo_total (float): Ativo total

    Returns:
        float: ROA em percentual
    """
    if ativo_total == 0:
        return 0
    return (lucro_liquido / ativo_total) * 100


def calcular_margem_bruta(receita, cmv):
    """
    Calcula margem bruta.

    Args:
        receita (float): Receita líquida
        cmv (float): Custo de Mercadoria Vendida

    Returns:
        float: Margem bruta em percentual
    """
    if receita == 0:
        return 0
    lucro_bruto = receita - cmv
    return (lucro_bruto / receita) * 100


# Constantes úteis
TAXA_IMPOSTO_PADRAO = 0.15
TAXA_SELIC_ANUAL = 0.1125
