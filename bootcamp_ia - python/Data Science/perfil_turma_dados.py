import pandas as pd
from perfil_tuma_funcoes import limpeza_idade, limpeza_altura, limpeza_semestre

df = pd.read_csv("Perfil da turma de IA.csv")

# remocao de coluna indesejada
df = df.drop(columns=['Carimbo de data/hora'])

# filtrando colunas numericas
numeric_columns = ['Idade', 'Semestre/Período' ,'Altura']

# chamando as funcoes de limpeza
df['Idade'] = df['Idade'].apply(limpeza_idade)
df['Altura'] = df['Altura'].apply(limpeza_altura)
df['Semestre/Período'] = df['Semestre/Período'].apply(limpeza_semestre)

# converte para número
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

df[numeric_columns].describe()
df[numeric_columns].isnull().sum()

print(df[numeric_columns])