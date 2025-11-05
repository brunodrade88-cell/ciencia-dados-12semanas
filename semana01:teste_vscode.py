# Teste do VS Code
print("Olá do VS Code!")

# Verificar ambiente
import sys
print(f"Python: {sys.executable}")

# Cálculo simples
capital = 10000
taxa = 0.12
montante = capital * (1 + taxa)
print(f"Montante: R$ {montante:,.2f}")
import pandas as pd
import numpy as np

# Criar DataFrame simples
dados = {
    'mes': ['Jan', 'Fev', 'Mar'],
    'receita': [100000, 120000, 115000]
}

df = pd.DataFrame(dados)
print(df)