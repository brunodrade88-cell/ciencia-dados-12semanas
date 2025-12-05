"""
Módulo de Análise Financeira

Funções para calcular indicadores financeiros de empresas.

Autor: Bruno Andrade
Data: 19/11/2025
"""

import numpy as np


def calcular_margem_liquida(receita, lucro):
    """Calcula margem líquida em percentual"""
    if receita == 0:
        return 0
    return (lucro / receita) * 100


def calcular_roe(lucro, patrimonio_liquido):
    """Calcula ROE (Return on Equity)"""
    if patrimonio_liquido == 0:
        return 0
    return (lucro / patrimonio_liquido) * 100


def calcular_liquidez_corrente(ativo_circulante, passivo_circulante):
    """Calcula liquidez corrente"""
    if passivo_circulante == 0:
        return float('inf')
    return ativo_circulante / passivo_circulante


def calcular_crescimento(valores):
    """Calcula crescimento percentual entre primeiro e último valor"""
    if len(valores) < 2:
        return 0

    inicial = valores[0] if isinstance(valores, np.ndarray) else valores.iloc[0]
    final = valores[-1] if isinstance(valores, np.ndarray) else valores.iloc[-1]

    if inicial == 0:
        return 0

    return ((final - inicial) / inicial) * 100


def classificar_margem(margem):
    """Classifica margem em categorias"""
    if margem >= 20:
        return "Excelente"
    elif margem >= 15:
        return "Boa"
    elif margem >= 10:
        return "Moderada"
    else:
        return "Baixa"


def classificar_liquidez(liquidez):
    """Classifica liquidez em categorias"""
    if liquidez >= 1.5:
        return "Saudável"
    elif liquidez >= 1.0:
        return "Adequada"
    else:
        return "Atenção"
