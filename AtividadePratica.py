'''num1 = int(input("digite um numero: "))
if num1 % 2 != 0:
    num1 += 1
num2 = int(input("digite outro numero: "))
par = 0
for numero in range(num1, num2, 2):
    if numero % 2 == 0 and num2 > num1 and num1 > 0 and num2 > 0:
        print(f"o numero {numero} é par")
        par += 1
    elif numero % 2 != 0 and num2 > num1 and num1 > 0 and num2 > 0:
        print(f"o numero {numero} é par")
        par += 1
    else:
        print("numeros invalidos")
        break
print(par)'''


'''soma = 0
for num in range(2, 31, 2):
    soma += num
    print(soma)'''

'''
soma = 0
for mes in range(1, 10):
    dinheiro = float(input('digite a quantidade que deseja economizar: '))
    soma += dinheiro
print(f"voce economizou {soma} no total de nove meses")'''

'''for i in range(1, 11):
    valor = float(input(f"digite o valor {i}: "))
    if valor > 50:
        print(f"o valor {valor} é maior que 50")
    else:
        print("o valor é menor ou igual a 50")'''

'''media = 0
for i in range(1, 31):
    resposta = input(f"digite a resposta do participante {i}: ")
    if resposta != "s" and resposta != "n":
        print('resposta invalida')
        resposta = input(f"digite a resposta do participante {i}: ")
    else:
        media += 1
if media >= 21:
    print("media alta")
elif media >= 12:
    print("media moderada")
elif media <= 12:
    print("media baixa")'''

'''nome_cliente = input("digite o nome do cliente: ")
sexo = input("digite o sexo do cliente: ")
camisas = int(input("digite a quantidade de camisas: "))
calças = int("digite a quantidade de cakças: ")
sapatos = int(input("digite a quantidade de sapatos: "))
if nome_cliente == 0 or sexo == 0 or camisas == 0 or calças == 0 or sapatos == 0:
    print("valor invalido")
    nome_cliente = input("digite o nome do cliente: ")
    sexo = input("digite o sexo do cliente: ")
    camisas = int(input("digite a quantidade de camisas: "))
    calças = int("digite a quantidade de cakças: ")
    sapatos = int(input("digite a quantidade de sapatos: "))
quantidade = 0
for i in range(camisas):
    for j in range(calças):
        for x in range(sapatos):
            print(camisas, calças, sapatos)
            quantidade += 1
print(f"a quantidade de possibilidades é {quantidade}")'''

