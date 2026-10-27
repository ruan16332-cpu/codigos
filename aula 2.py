'''lista_idades = []
for i in range(1,9):
    idades = float(input(f"digite a idade {i}: "))
    lista_idades.append(idades)
for m in lista_idades:
    print( m, end= "|")
print("\n")
print(f"a maior idade digitada foi: {max(lista_idades)} ")
print(f"a menor idade digitada foi: {min(lista_idades)}")
print(f"a soma de todas as idades é: {sum(lista_idades)}")
print(f"a media das idades é: {sum(lista_idades)/len(lista_idades)} ")'''

lista_notas = []
aprovados = 0
reprovados = 0
for alunos in range(1, 11):
    notas_alunos = float(input(f"digite a nota do aluno {alunos}: "))
    lista_notas.append(notas_alunos)
print(f"a media da turma é: {sum((lista_notas / len(lista_notas)))}")
print(f"a maior nota da turma é: {max(lista_notas)}")
print(f"a menor nota da turma é: {min(lista_notas)}")
for m in lista_notas:
    if m >= 7:
        aprovados += 1
    else:
        reprovados += 1
print(f"a quantidade de alunos aprovados é {aprovados} \n a quantidade de alunos reprovados é {reprovados}")

