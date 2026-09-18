# Crie um algoritmo em Python onde haverá uma função para realizar
# operações matemáticas. Essa função deve implementar soma, subtração,
# multiplicação e divisão. Como parâmetro, deve receber a informação de
# qual operação deverá ser executado, e a operação deverá ocorrer em todos
# os números recebidos por ela. Por exemplo, caso eu envie a informação de
# soma e os números 2, 5, 8 e 10, o resultado deve ser 2+5+8+10. Não há limites
# de números que devem ser passados como parâmetros, e se o tipo de operação não
# ser informado, deve-se utilizar como padrão a soma. (Verificações: retornar
# erro ao verificar que haverá divisão por 0)

def calculos_matematicos (operacao, *numeros):

    if operacao == "soma":
        total = 0
        for num in numeros:
            total += num

    elif operacao == "subtracao":
        for num in numeros[1:]:
            total = numeros[0]
            total -= num

    elif operacao == "multiplicacao":
        total = 1
        for num in numeros:
            total *= num
            
    elif operacao == "divisao":
        for num in numeros[1:]:
            total = numeros[0]
            total /= num

    else: 
        return "Operador inválido"

    return total

print(calculos_matematicos("multiplicacao", 3, 10, 20))
