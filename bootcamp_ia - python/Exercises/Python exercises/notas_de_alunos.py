# Faça um código em Python onde o usuário deve informar a quantidade de alunos que ele irá cadastrar, 
# depois crie um loop para adicionar todos os alunos, devendo informar o nome e em seguida a nota do aluno. 
# O sistema deve processar as informações e retornar uma lista de dicionários ou tuplas com todos os alunos. 

# Depois retorne uma lista de dicionários ou tuplas contendo os alunos que foram aprovados (nota 60 ou maior), 
# outra de alunos que ficaram de recuperação (nota entre 40 e baixo de 60). E a última de alunos que reprovaram. 
# Todas as listas devem estar ordenadas em ordem de chamada e deve conter o número da chamada, nome e nota.

print("\n", 15*"-=", "CADASTRO DE NOTAS / ALUNOS", 15*"-=")

qnt_cadastro = int(input("Quantidade de cadastros: "))
notas_alunos = []

for i in range(qnt_cadastro):
    aluno = input(f"Nome do {[i+1]}º aluno: ")
    nota = float(input(f"Nota do {[i+1]}º aluno: "))

    notas_alunos.append([aluno, nota])

dicionario_resultado = dict(notas_alunos)

alunos_aprovados = {}
alunos_reprovados = {}
alunos_recuperacao = {}


for aluno_dicionario, nota_dicionario in dicionario_resultado.items():
    if nota_dicionario >= 60:
        alunos_aprovados[aluno_dicionario] = nota_dicionario

    elif 40 >= nota_dicionario < 60:
        alunos_recuperacao[aluno_dicionario] = nota_dicionario

    else:
        alunos_reprovados[aluno_dicionario] = nota_dicionario


aprovados_chamada = dict(sorted(alunos_aprovados.items()))
reprovados_chamada = dict(sorted(alunos_reprovados.items()))
recuperacao_chamada = dict(sorted(alunos_recuperacao.items()))


resultados_alunos = [aprovados_chamada, reprovados_chamada, recuperacao_chamada]
print("\n", 15*"-=", "RESULTADO DOS ALUNOS / NOTA", 15*"-=")
print(resultados_alunos, "\n")


# Adicionar em cada aluno o resultado de sua nota e printar no terminal de forma organizada
print("TABELA DE RESULTADOS - ALUNOS / NOTAS")
print(f"{'Aluno':<10} | {'Nota':<6} | Situação")
print("-" * 32)

for grupo in resultados_alunos:
    for aluno, nota in grupo.items():

        if nota >= 60:
            situacao = "Aprovado"
        elif 40 <= nota < 60:
            situacao = "Recuperacao"
        else:
            situacao = "Reprovado"

        print(f"{aluno:<10} | {nota:<6.1f} | {situacao}")