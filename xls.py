import pandas as pd

tabela_pessoas = pd.read_excel("planilha.xlsx")

pd.set_option("display.max_columns", None)

# print(tabela_pessoas)

qtdPessoas = tabela_pessoas[['Nome']].count()

print(qtdPessoas)