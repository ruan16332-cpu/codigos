'''idade = int(input('digite sua idade: '))
autorizacao = input('digite se voce tem autorização: ')
genero = input("digite seu gênero: ")

if idade >= 18:
    if autorizacao == 'sim' or autorizacao == 'y' or autorizacao == '1':
        print("acesso autorizado.")
        if genero == "masculino" or genero == 'm':
            print('Setor Acer')
        elif genero == 'feminino' or genero == 'f':
            print("Setor TCL")
        else:
            print("genero invalido")

    elif autorizacao == 'nao' or autorizacao == 'n' or autorizacao == '2':
        print("acesso negado.")
    else:
        print('autorização inválida.')
else:
    print("idade não permitida")'''

'''print(" 1- Cadastro de Aluno e Notas\n 2- Cursos e Disciplinas \n 3- Horários")
op = int(input("digite a opção desejada: "))
match op:
    case 1:
        nome = input("digite o nome do aluno: ")
        nota1 = float(input("digite a nota do aluno: "))
        nota2 = float(input("digite a nota do aluno: "))
        media = (nota1 + nota2) / 2
        if media >= 7:
            print("aprovado")
        else:
            print("reprovado")
    case 2:
        print("Cursos")
    case 3:
        print("Horários")
    case _:
        print("opção invalida.")'''

      

