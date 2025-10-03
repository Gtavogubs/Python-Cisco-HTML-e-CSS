import pandas as pd
from openpyxl import load_workbook

def calcular_imc(peso, altura):
    """Calcula o IMC dado o peso (KG) e altura (m)."""
    return round(peso / (altura ** 2), 2)

def classificar_imc(imc):
    """Classifica o IMC de acordo com as faixas padrão."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

arquivo = "dados_pessoas.xlsx"

try:
    dados = pd.read_excel(arquivo)
    dados.columns = dados.columns.astype(str).str.strip()

    if not {'Nome', 'Peso', 'Altura'}.issubset(dados.columns):
        print("O arquivo Excel deve conter as colunas: Nome, Peso e Altura")
    else:
        dados['Peso'] = pd.to_numeric(dados['Peso'], errors='coerce')
        dados['Altura'] = pd.to_numeric(dados['Altura'], errors='coerce')  # corrigido aqui

        dados = dados.dropna(subset=['Peso', 'Altura'])

        dados['IMC'] = dados.apply(lambda x: calcular_imc(x['Peso'], x['Altura']), axis=1)
        dados['Classificação'] = dados['IMC'].apply(classificar_imc)

        with pd.ExcelWriter(arquivo, engine='openpyxl', mode='w') as writer:
            dados.to_excel(writer, sheet_name="Pessoas", index=False)

        print(f"Resultados adicionados ao arquivo '{arquivo}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")