#comparar idade
seu_nome = input('digite seu nome: ')
nome_amigo = input('digite o nome dele: ')
sua_idade = int(input('digite a sua idade'))
idade_amigo = int(input('digite a idade dele'))

if sua_idade > idade_amigo and idade_amigo > 0 and sua_idade > 0:
    print('você é mais velho que seu amigo. ')
elif sua_idade < idade_amigo and sua_idade > 0 and idade_amigo > 0:
    print('seu amigo é mais velho que você.')
else:
    print("idade inválida inserida")


#radar de avenida
velocidade_veiculo = float(input('a velocidade do veículo é de: '))

if velocidade_veiculo > 60:
    print('veículo multado, velocidade excedida.')
else:
    print('velocidade normal.')


#programa de loja
produto = input('digite o nome do produto: ')
preco = float(input('digite o preço do produto: '))

if preco > 200:
    preco *= 0.90
    print(f"o preço do produto {produto} foi descontado para o preço de {preco:.2f}")
elif preco < 200 and preco > 0:
    preco -= 30
    print(f'o preço do produto {produto} é {preco:.2f}')
else:
    print("valor inválido")


