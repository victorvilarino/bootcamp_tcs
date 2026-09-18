import pandas as pd

df = pd.read_csv("Perfil da turma de IA.csv")

df = df.drop(columns=['Carimbo de data/hora'])

df.isna().sum() # Conta quantos valores Null

df['Idade'] = pd.to_numeric(df['Idade'], errors='coerce') # Converte para número

