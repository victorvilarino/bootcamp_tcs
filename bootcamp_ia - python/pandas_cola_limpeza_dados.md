# Pandas — Cola Rápida para Limpeza de Dados

## 1. Importar o Pandas

```python
import pandas as pd
```

---

## 2. Ler um arquivo CSV

```python
df = pd.read_csv("arquivo.csv")
```

Se o separador for `;`:

```python
df = pd.read_csv("arquivo.csv", sep=";")
```

> `df` significa DataFrame: a tabela que será manipulada pelo Pandas.

---

## 3. Inspecionar os dados

```python
df.head()       # Mostra as 5 primeiras linhas
df.tail()       # Mostra as 5 últimas linhas

df.shape        # Retorna (quantidade de linhas, quantidade de colunas)
df.columns      # Mostra os nomes das colunas
df.dtypes       # Mostra o tipo de cada coluna
df.info()       # Resumo geral do DataFrame
df.describe()   # Estatísticas das colunas numéricas
```

---

## 4. Selecionar colunas

Uma coluna:

```python
df["Idade"]
```

Várias colunas:

```python
df[["Idade", "Filme"]]
```

---

## 5. Remover colunas

Uma coluna:

```python
df = df.drop(columns=["Nome"])
```

Várias colunas:

```python
df = df.drop(columns=["Nome", "Email", "Data"])
```

Alterando o próprio DataFrame:

```python
df.drop(columns=["Nome"], inplace=True)
```

---

## 6. Valores ausentes

Ver onde existem valores nulos:

```python
df.isnull()
```

Contar valores nulos por coluna:

```python
df.isnull().sum()
```

Remover linhas com valores nulos:

```python
df = df.dropna()
```

Preencher valores nulos:

```python
df["Idade"] = df["Idade"].fillna(18)
```

---

## 7. Duplicados

Verificar linhas duplicadas:

```python
df.duplicated()
```

Contar duplicados:

```python
df.duplicated().sum()
```

Remover duplicados:

```python
df = df.drop_duplicates()
```

---

## 8. Ver valores únicos

```python
df["Comida"].unique()
```

Útil para encontrar dados inconsistentes, como:

```text
Pizza
pizza
PIZZA
```

---

## 9. Contar valores

```python
df["Comida"].value_counts()
```

Exemplo de resultado:

```text
pizza         12
hamburguer     7
lasanha        4
```

---

## 10. Padronizar textos

Transformar em minúsculas:

```python
df["Comida"] = df["Comida"].str.lower()
```

Transformar em maiúsculas:

```python
df["Comida"] = df["Comida"].str.upper()
```

Remover espaços no começo e no fim:

```python
df["Comida"] = df["Comida"].str.strip()
```

---

## 11. Filtrar dados

Pessoas com 18 anos ou mais:

```python
df[df["Idade"] >= 18]
```

Somente quem respondeu pizza:

```python
df[df["Comida"] == "pizza"]
```

Duas condições:

```python
df[(df["Idade"] >= 18) & (df["Comida"] == "pizza")]
```

Operadores comuns:

```text
==   igual
!=   diferente
>    maior
<    menor
>=   maior ou igual
<=   menor ou igual

&    E
|    OU
```

---

## 12. Converter tipos

Converter para número:

```python
df["Idade"] = pd.to_numeric(df["Idade"])
```

Se existirem valores inválidos:

```python
df["Idade"] = pd.to_numeric(df["Idade"], errors="coerce")
```

`errors="coerce"` transforma valores que não podem ser convertidos em `NaN`.

---

## 13. Renomear colunas

```python
df = df.rename(columns={
    "Qual a sua idade?": "Idade",
    "Qual seu filme favorito?": "Filme"
})
```

---

## 14. Ordenar dados

Ordenar por uma coluna:

```python
df = df.sort_values("Idade")
```

Ordem decrescente:

```python
df = df.sort_values("Idade", ascending=False)
```

---

## 15. Salvar o resultado

```python
df.to_csv("arquivo_limpo.csv", index=False)
```

O `index=False` evita salvar a coluna de índice:

```text
0
1
2
3
...
```

---

# Fluxo básico de limpeza

```python
import pandas as pd

df = pd.read_csv("pesquisa.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

df = df.drop_duplicates()

df["Comida"] = df["Comida"].str.strip().str.lower()

print(df["Comida"].value_counts())

df.to_csv("pesquisa_limpa.csv", index=False)
```

---

# Comandos que vale lembrar primeiro

```python
pd.read_csv()

df.head()
df.info()
df.shape
df.columns

df["coluna"]

df.drop()
df.dropna()
df.drop_duplicates()

df.isnull().sum()

df["coluna"].unique()
df["coluna"].value_counts()

df["coluna"].str.lower()
df["coluna"].str.strip()

df.to_csv()
```

---

## Caminhos de arquivo

Se o `.py` e o `.csv` estiverem na mesma pasta:

```python
df = pd.read_csv("Perfil da turma de IA.csv")
```

Evite repetir pastas que já fazem parte do diretório atual.

No PowerShell, para verificar a pasta atual:

```powershell
pwd
```

