'''numeros = []
cont = 1 
while cont == 1: 
    numero = float(input("digite um numero: "))
    numeros.append(numero)
    cont = int(input("deseja continuar? 1-Sim 2-Não"))
    if cont == 2:
        break
print(numeros)'''

'''L = [1,2,3,7,8,9,10,11,12]
tamanho = len(L)
for x in tamanho:
    print(L[x])'''

'''A = ['mouse', 'teclado', 'monitor', 'estabilizador']
B = ['memoria', 'cpu', 'ssd', 'chipset', 'rom']
A.append(B)
print(A)'''

'''A = ['Python', 'Java', 'C', 'PHP', 'JavaScript', 'Dart']
B = ['C++', 'Python', 'Java', 'Julia', 'Go', 'JavaScript']
C = []
for x in A:
    if x not in C:
        C.append(x)
for x in B:
    if x not in C:
        C.append(x)
print(C)'''

'''L = [15, 7, 27, 39]
p = int(input("digite um valor a procurar: "))
for i, v in enumerate(L):
    if p == v:
        print(f"o valor {p} foi encontrado na posição {i}")
        break
else:
    print(f"o valor {p} não foi encontrado")'''

'''T = []
for i, v in enumerate[T]:
    print(f"indice: {i}, valor: {v}")'''

lista_numeros = []
lista_palavras = []
cont = 0
while True:
    p = input("digite um numero ou palavra a ser adicionada na lista ou digite 0 para parar: ")
    if p == '0':
        break
    elif p.isdigit():
        lista_numeros.append(p)
    elif p.isalpha():
        lista_palavras.append(p)
    cont += 1
print(lista_palavras)
print(lista_numeros)
print(f"voce digitou {cont} vezes")


