servidores = [
    ["Servidor01", 35, 120],
    ["Servidor02", 82, 450],
    ["Servidor03", 67, 280],
    ["Servidor04", 91, 520],
    ["Servidor05", 45, 180],
    ["Servidor06", 76, 350]
]


print("===total conexões===")
def total_conexões(x):
    total = 0
    for conexões in x:
        total += conexões[2]
    return total
print(f"o total de dispositivos conectados aos servidores é: {total_conexões(servidores)}")
print("===media uso de cpu===")
def media_cpu(x):
    media_total = 0
    uso_total = 0
    for uso_cpu in x:
        uso_total += uso_cpu[1]
    media_total = uso_total / len(x)
    return media_total
print(f"a media total de uso de CPU é: {media_cpu(servidores):.2f}%")
print("===maior uso de cpu===")
def maior_uso(x):
    maior = x[0][1]
    for processamento in x:
        if processamento[1] > maior:
            maior = processamento[1]
    return maior
print(f"o maior uso de CPU é {maior_uso(servidores)}%")
print("===menor uso de cpu===")
def menor_uso(x):
    menor = x[0][1]
    for processamento in x:
        if processamento[1] < menor:
            menor = processamento[1]
    return menor
print(f"o menor uso de CPU é {menor_uso(servidores)}%")
print("===servidores com cpu acima da media===")
def cpu_maior(x):
    for processamento in servidores:
        if processamento[1] > media_cpu(x):
            print(f"ALERTA! o servidor {processamento[0]} está com o uso de CPU acima da média.")
cpu_maior(servidores)
print("===servidores com sistema acima da media===")
def sobrecarregado(x):
    for processamento in servidores:
        if processamento[1] > 80 or processamento[2] > 400:
            print(f"ALERTA! o servidor {processamento[0]} está sobrecarregado.")
sobrecarregado(servidores)
print()
print("===servidor com maior quantidade de conexões===")
def maior_conexoes(x):
    maior = x[0][2]
    servidor = x[0][0]
    for conexoes in x:
        if conexoes[2] > maior:         
            maior = conexoes[2]
            servidor = conexoes[0]
    return f'o servidor com a maior quantidade de conexões simultaneas é o {servidor} com {maior} conexões simultaneas'
print(maior_conexoes(servidores))

print("===Calculo de Salarios===")
def calculo_salario(x):
    salario_incremento = x * 1.125
    salario_imposto = x * 0.07
    salario_final = salario_incremento - salario_imposto
    return salario_final

for funcionarios in range(1, 11):
    funcionario = input("digite o nome do funcionario: ")
    funcao = input(f"digite a função do funcionario {funcionario}: ")
    salario_antigo = float(input(f'digite o salario atual do funcionario {funcionario}: '))
    print(f"o funcionário {funcionario}, com função de {funcao}, terá um salário novo de {calculo_salario(salario_antigo):.2f}")

