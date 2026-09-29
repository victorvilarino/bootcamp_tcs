# Loja de sapatos:
# 1) Leia a quantidade de sapatos.
# 2) Leia os tamanhos disponíveis.
# 3) Use Counter para contar quantos sapatos existem de cada tamanho.
# 4) Leia a quantidade de clientes.
# 5) Para cada cliente, leia: tamanho desejado e preco oferecido.
# 6) Se houver esse tamanho em estoque, some o preco ao total e retire 1 do estoque.
# 7) No final, imprima o total arrecadado.

from collections import Counter

qnt_sapatos = int(input())

tamanho_sapatos = list(map(int, input().split()))
estoque = Counter(tamanho_sapatos)

qnt_clientes = int(input())
total_arrecadado = 0

for _ in range(qnt_clientes):
    tamanho_cliente, preco_cliente = map(int, input().split())
    
    if estoque[tamanho_cliente] > 0:
        total_arrecadado += preco_cliente
        estoque[tamanho_cliente] -= 1

print(total_arrecadado)