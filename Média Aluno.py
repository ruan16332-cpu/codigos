aluno = input("digite o nome do aluno: ")
soma = 0
divisao = 0
for i in range(1, 5):
    nota = float(input(f"digite a nota {i} do aluno {aluno}: "))
    soma += nota
    divisao += 1
    if nota < 0 or nota > 10:
        print("nota invalida")
        break
media = soma / i
print(f'a média do aluno {aluno} é {media}')
if media == 10:
    print("nota excelente")
elif media >= 7:
    print("aprovado")
elif media >= 1:
    print("recuperação")
elif media == 0:
    print("reprovado")
    


            
                 

