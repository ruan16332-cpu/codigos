#fatorial
'''numero = int(input("digite um numero: "))
fatorial = 1
for i in range(numero, 1, -1):
    fatorial *= i
    print(fatorial)
print(f"o fatorial do numero {numero} é {fatorial}")'''

#igualdade de paises
'''paisA = 90000
paisB = 200000
anos = 0
while paisA != paisB:
    paisA *= 0.05
    paisB *= 0.015
    anos += 1

print(f'em {anos} anos, os dois paises terão a mesma quantidade de habitantes')'''


#notas alunos
'''notas = []
aprovados = 0
recuperação = 0
reprovados = 0

while True:
    
    nota = float(input("digite a nota do aluno: "))
    while nota < 0 or nota > 10:
        print("nota invalida")
        nota = float(input("digite a nota do aluno: "))
    notas.append(nota)
    
    if nota >= 7:
        print("aluno aprovado")
        aprovados +=1 
    elif nota >= 5:
        print("aluno em recuperação")
        recuperação += 1
    elif nota < 5:
        print("aluno reprovado")
        reprovados += 1
    else:
        print("algo deu errado")
    
    cont = int(input('deseja adicionar uma nota?(1-Sim, 2-Não) '))
    if cont == 2:
        break

quantidade_alunos = len(notas)
media_turma = sum(notas) / quantidade_alunos

porc_aprovados = (aprovados / quantidade_alunos ) * 100
porc_recuperacao = (recuperação / quantidade_alunos) * 100
porc_reprovados = (reprovados /quantidade_alunos ) * 100

print(f"Total de alunos avaliados: {quantidade_alunos}")
print(f"Média geral da turma: {media_turma:.2f}")
print(f"Aprovados (≥ 7.0): {aprovados} ({porc_aprovados:.1f}%)")
print(f"Recuperação (5.0 a 6.9): {recuperação} ({porc_recuperacao:.1f}%)")
print(f"Reprovados (< 5.0): {reprovados} ({porc_reprovados:.1f}%)")
print(f"A maior nota foi {max(notas):.1f}")
print(f"A menor nota foi {min(notas):.1f}")'''

# Seleção de atributos para um modelo
n = int(input("digite a quantidade total de atributos: "))
r = int(input("digite a quantidade de atributos a selecionar: "))
if r < 0 or r > n:
    print("o valor de atributos a selecionar não pode ser menor que 0 e nem maior que a quantidade total de atributos: ")
else:
    fat_n = 1 
    for i in range(2, n + 1):
        fat_n *= i

    fat_r = 1
    for i in range(2, r + 1):
        fat_r *= i

    fat_n_r = 1
    for i in range(2, (n - r) + 1):
        fat_n_r *= i

    combinacoes = fat_n // (fat_r * fat_n_r)
    print(f"Total de subconjuntos possíveis C({n}, {r}): {combinacoes:,}")
    limite_variavel = 10000
    if combinacoes <= limite_variavel:
        print("Status de Viabilidade: **VIÁVEL** para busca exaustiva (<= 10.000 combinações).")
    else:
        print("Status de Viabilidade: **INVIÁVEL** para busca exaustiva (> 10.000 combinações)")
    