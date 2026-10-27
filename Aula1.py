'''
aluno = input("digite o nome do aluno: ")
soma = 0
divisao = 0
for i in range(1, 5):
    nota = float(input(f"digite a nota {i} do aluno {aluno}: "))
    soma += nota
    divisao += 1
print(f'a média do aluno {aluno} é {soma / divisao}')
'''

'''
coxinhas = int(input('digite a quantidade de coxinhas: '))
sobra = coxinhas % 4
divisao = coxinhas // 4
print(f'para grupo de 4 pessoas, sobraria(m) {coxinhas % 4} coxinha(s)')
'''

base = float(input("digite a base do triangulo: "))
altura = float(input("digite a altura do triangulo: "))
area = (base * altura) / 2

print(f'a area do triangulo é {area}')
