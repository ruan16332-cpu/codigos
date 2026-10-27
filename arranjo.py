
from itertools import permutations

elementos = [1,2,3,4,5,6,7]
tamanho = 7

arranjo = permutations(elementos, tamanho)
tentativa = 1
for p in arranjo:
    print(p)
    print(f"tentativa numero:{tentativa}\n")
    tentativa += 1


'''

numeros = [0, 1, 2, 3, 4, 5, 6]
tamanho = 3

arranjo_repeticao = product(numeros, repeat=tamanho)
tentativa = 1

for combo in arranjo_repeticao:
    print(combo)
    print(f"tentativa numero:{tentativa}\n")
    tentativa += 1'''

