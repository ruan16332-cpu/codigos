#calculo media, mediana e moda de idades
def media(x):
    calculo_media = sum(x)/len(x)
    return(calculo_media)

def mediana(x):
    lista_ordenada = sorted(x)
    tamanho = len(lista_ordenada)
    meio = tamanho // 2
    if tamanho % 2 != 0:
        return(lista_ordenada[meio])
    else:
        return((lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2)

def moda(x):
    
    calculo_moda = max(x, key= x.count)
    return calculo_moda

lista_idades = []
for pessoa in range(1, 11):
    idade = int(input(f"digite a idade da pessoa {pessoa}: "))
    lista_idades.append(idade)
print(f"a media das idades é: {media(lista_idades)}")
print(f"a mediana das idades é: {mediana(lista_idades)}")
print(f"a moda das idades é: {moda(lista_idades)}")


#calculo de probabilidade de uma bola especifica
bolas = ['vermelha', 'azul', 'verde', 'vermelha', 'amarela', 'azul', 'vermelha', 'verde', 'azul', 'vermelha']
def probabilidade(x):
    total = len(x)
    favoraveis  = x.count('vermelha')
    calculo_probabilidade = favoraveis / total
    a, b = favoraveis, total
    while b != 0:
        a, b = b, a % b
    mdc = a 
    fracao = f'{favoraveis // mdc} / {total // mdc}'
    porcentagem = favoraveis / total
    print(f"Fração simplificada: {fracao}")
    print(f"Porcentagem: {porcentagem:.2%}")
probabilidade(bolas)



#calculo geral da turma
def media_aluno(x):

    calculo_media = (x[1] + x[2] + x[3]) / 3
    estado = ""
    if calculo_media >= 7:
        estado = "aprovado"
    elif calculo_media >= 0:
        estado = 'reprovado'
    return f'{x[0]}: {calculo_media:.1f}, {estado}'
def media_turma(x):
    soma_medias = 0
    for aluno in x:
        calculo_media = (aluno[1] + aluno[2] + aluno[3]) / 3
        soma_medias += calculo_media
    media_geral = soma_medias / len(x)
    return f'a media da turma é: {media_geral:.1f}'
def destaques(x):
    primeiro_aluno = x[0]
    maior_media = (primeiro_aluno[1] + primeiro_aluno[2] + primeiro_aluno[3]) / 3
    nome_maior = primeiro_aluno[0]

    menor_media = maior_media
    nome_menor = nome_maior
    for aluno in x:
        media_atual = (aluno[1] + aluno[2] + aluno[3]) / 3
        if media_atual > maior_media:
            maior_media = media_atual
            nome_maior = aluno[0]
        elif media_atual < menor_media:
            menor_media = media_atual
            nome_menor = aluno[0]
    resultado = (
        f'o alundo com a maior media é: {nome_maior}, {maior_media:.1f}\n'
        f'o aluno com a menor media é: {nome_menor}, {menor_media:.1f}'        
    )
    return resultado

alunos = []
while True:
    aluno = input("digite o nome e as 3 notas do aluno: ")
    if aluno.lower() == 'sair':
        break
    #transforma o texto em lista
    itens = aluno.split()
    lista_interna = []
    #transforma o numero(string) em float
    for item in itens:
        try:
            lista_interna.append(float(item))
        except ValueError:
            lista_interna.append(item)
    alunos.append(lista_interna)
print("===nome dos alunos===")
for nome in alunos:
    print(nome[0], end= "|")
print('\n')
print("===media dos alunos===")
print("a media de cada aluno é:")
for aluno_indv in alunos:
    print(media_aluno(aluno_indv))
print('\n')
print("===media da turma===")
print(media_turma(alunos))
print('\n')
print("===alunos destaques===")
print(destaques(alunos))
print('\n')
print("===alunos aprovados e reprovados===")
aprovados = 0
reprovados = 0
if media_aluno >= 7:
    aprovados += 1
elif media_aluno >= 0:
    reprovados += 1
print(f"a quantidade de alunos aprovados é: {aprovados} aprovados")
print(f"a quantidade de alunos reprovados é: {reprovados} reprovados")


#aumentod e valor na compra
def acrescimo(x):
    novo_valor = []
    for preco in x:
        novo_valor.append(preco * 1.10)
    print(novo_valor)
precos = [50, 80, 120, 35, 200, 75]
acrescimo(precos)


#calculo de valor de estacionamento
def cobranca(a):
    novo_valor = 0
    if a <= 1:
        novo_valor = 5
    elif a > 1:
        novo_valor = 10
    elif a > 3:
        novo_valor = 15
    elif a > 5:
        novo_valor = 20
    return novo_valor

tempo_estacionado = int(input("digite o tempo que ficou estacionado: "))
print(f"o valor final pelo tempo estacionado é: {cobranca(tempo_estacionado)}")


#calculo de idade
def calculo(a, b):
    idade = a - b
    return idade

ano_nasc = int(input("digite o ano de seu nascimento: "))
ano_atual = int(input("digite o ano atual: "))
print(f"a sua idade é: {calculo(ano_atual, ano_nasc)} anos")

#calculo de areas
def area_triangulo(h, b):
    calculo_area = (b * h) / 2
    return calculo_area
def area_trapezio(B, b):
    calculo_area = (B + b) / 2
    return calculo_area
def area_losango(D,d):
    calculo_area = (D * d) / 2
    return calculo_area

print("digite 1-Triangulo, 2-Trapezio e 3-Losango")
opc = int(input("digite a opção que deseja: "))
match opc:
    case 1:
        altura = float(input("digite a altura do triangulo: "))
        base = float(input("digite a base do triangulo: "))
        print(f"a área do triangulo é: {area_triangulo(altura, base)}")
    case 2: 
        base_maior = float(input("digite a base maior do trapezio: "))
        base_menor = float(input("digite a base menor do trapezio: "))
        print(f"a area do trapezio é: {area_trapezio(base_maior, base_menor)}")
    case 3:
        diagonal_maior = float(input("digite a diagonal maior do losango: "))
        diagonal_menor = float(input("digite a diagonal menor do losango: "))
        print(f"a area do losango é: {area_losango(diagonal_maior,diagonal_menor)}")
    case _:
        print("digite novamente")


#verifficação de senha
def verificacao(x):
    tamanho = len(x)
    tem_8_caracteres = False
    if tamanho < 8:
        tem_8_caracteres = False
    else:
        tem_8_caracteres = True
    return tem_8_caracteres

senha = input("digite sua senha: ")
print(f"{verificacao(senha)}")
