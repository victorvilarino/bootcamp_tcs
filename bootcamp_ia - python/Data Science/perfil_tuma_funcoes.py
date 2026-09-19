def limpeza_idade (valor):
    valor_limpo = valor.split(" ")[0]

    return int(valor_limpo)


def limpeza_altura (valor):
    valor = valor.lower()
    valor = valor.replace(",", ".")

    valor = valor.replace("cm", "")
    valor = valor.replace("m", "")
    valor = valor.replace("c", "")

    valor_limpo = valor.split(" ")[0]

    if 1 < float(valor_limpo) < 2.0:
        return valor_limpo

    else:
        valor_limpo = float(valor_limpo) / 100
        return float(valor_limpo)


def limpeza_semestre (valor):
    valor = valor.lower()
    valor_list = valor.split()

    for num_letra in valor_list:
        if num_letra == "sexto":
            return 6

        elif num_letra == "segundo":
            return 2

    for num in valor:
        if num.isdigit():
            return int(num)