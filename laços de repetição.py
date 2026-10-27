'''
controlador = 's'
while controlador == 's':
    valor = float(input('digite o valor da venda: ')
    percentual_comissao = float(input('digite o percentual da comissão: ')
    comissao = valor * percentual_comissao
    print(f'a comissão será de RS{comissao:.2f}')
    controlador = input('deseja fazer outro calculo? ')
print('programa encerrado')
'''
'''
nivel_oceano = 0
for ano in range(1, 26):
    nivel_oceano += 1.6
print(f'em 25 anos, o nivel do oceano estará {nivel_oceano:.2f} milimetros maior')
'''

'''peso = float(input('digite o seu peso: '))
for mes in range(1,7):
    peso -= 1.8
print(f'apos seis meses, voce terá perdido {peso:.2f}Kg')'''

'''for vestido in ['branco', 'azul']:
    for sapato in ['preto', 'marrom']:
        print(vestido,sapato)'''
'''   
for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)'''


'''
aluno = input("digite o nome do aluno: ")
nota = 0
while nota >= 0:
    nota = float(input(f"digite a nota do aluno {aluno}: "))
    if nota < 0 or nota > 10:
        print("nota invalida, tente novamente")
        break
    elif nota == 10:
        print("nota perfeita")
    elif nota >= 7:
        print("aprovado")
    elif nota <= 6:
        print("recuperação")'''

'''num1 = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))
while num1 < (num2 - 1):
    num1 += 1
    print(num1)'''

nome_aluno = input('digite o nome do aluno: ')
quantidade_notas = int(input('digite a quantidade de notas que deseja aplicar: '))
media = 0
repeticao = 1
while repeticao <= quantidade_notas:
    nota = float(input(f'digite a nota do aluno {nome_aluno}: '))
    media += nota
    repeticao += 1
resultado = media / quantidade_notas
print(f'o aluno {nome_aluno} tem média {resultado}')
