import math
#teste de numero impar e par
num = int(input('digite um numero: '))
if num % 2 == 0:
    print("numero par")
else:
    print('numero impar')


#calssificador de idade
idade = int(input("digite sua idade"))
if idade >= 65:
    print("você é idoso(a)")
elif idade >= 18:
    print('você é adulto(a)')
elif idade >= 13:
    print("você é adolescente")
elif idade >= 0:
    print("você é criança")
else:
    print("idade invalida")


#mini calculadora
num1 = float(input("digite um numero: "))
operacao = input("digite qual operação deseja: ")
num2 = float(input("digite um numero: "))

match operacao:
    case "+":
        calculo = num1 + num2
        print(f"seu resultado é: {calculo}")
    case "-":
        calculo = num1 - num2
        print(f"seu resultado é: {calculo}")
    case "*":
        calculo = num1 * num2
        print(f"seu resultado é: {calculo}")
    case "%":
        calculo = num1 / num2
        print(f"seu resultado é: {calculo}")
    case "_":
        print("digite uma operação valida")


#calssificação triangulo
lado1 = float(input("digite um lado do triangulo: "))
lado2 = float(input("digite um lado do triangulo: "))
lado3 = float(input("digite um lado do triangulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("esse triangulo existe.")
    if lado1 == lado2 == lado3:
        print("seu triangulo é Equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("seu triangulo é Isoceles")
    else:
        print("seu triangulo é Escaleno")
else:
    print("esse triangulo não existe.")


#calculo de raizes reais
a = int(input("digite o valor de a: "))
b = int(input("digite o valor de b: "))
c = int(input("digite o valor de c: "))
delta = (b ** 2) - (4 * a * c)
print(f"O valor de delta é: {delta}")
valor_x1 = b + delta ** 0.5 / 2 * a
valor_x2 = b - delta ** 0.5 / 2 * a
if delta > 0:
    print(f"há duas raizes reais distintas: {valor_x1:.3f}, {valor_x2:.3f}")
elif delta == 0:
    print(f"há uma raiz real ou duas raizes reais iguais: {valor_x1:.3f}, {valor_x2:.3f}")
elif delta < 0:
    print("não há uma raiz real")
else:
    print("que?")



#teste temperatura
temp_agua = float(input("digite a temperatura da agua em graus celsius: "))

if temp_agua >= 100:
    print("agua em estado gasoso")
elif temp_agua > 0:
    print("agua em estado liquido")
elif temp_agua <= 0:
    print("agua em estado solido")
else:
    print("temperatura invalida (como?)")


#comissao de empresa
funcionario = input("digite o nome do funcionario: ")
valor_venda = float(input("digite o valor da venda do funcionario: "))

if valor_venda > 1_000_000:
    comissao = valor_venda * 0.12
    print(f" o funcionario {funcionario}\n com {valor_venda} reais de vendas totais\n recebe {comissao} reais de comissão.")
elif valor_venda > 700_000:
    comissao = valor_venda * 0.10
    print(f" o funcionario {funcionario}\n com {valor_venda} reais de vendas totais\n recebe {comissao} reais de comissão.")
elif valor_venda > 500_000:
    comissao = valor_venda * 0.085
    print(f" o funcionario {funcionario}\n com {valor_venda} reais de vendas totais\n recebe {comissao} reais de comissão.")
elif valor_venda <= 500_000:
    comissao = valor_venda * 0.06
    print(f" o funcionario {funcionario}\n com {valor_venda} reais de vendas totais\n recebe {comissao} reais de comissão.")


#taxa de hospedagem
nome_hospede = input('digite o nome do hóspede')
dias = int(input("digite a quantidade de dias que o hospede ficou hospedado."))
if dias > 7:
    calculo = (dias * 290) + (dias * 6.5)
    print(f"o hospede {nome_hospede} terá que pagar {calculo:.2f}reais. ")
elif dias == 7:
    calculo = (dias * 290) + (dias * 12)
    print(f"o hospede {nome_hospede} terá que pagar {calculo:.2f}reais. ")
elif dias < 7:
    calculo = (dias * 290) + (dias * 16.5)
    print(f"o hospede {nome_hospede} terá que pagar {calculo:.2f}reais. ")
else:
    print("que isso?")

