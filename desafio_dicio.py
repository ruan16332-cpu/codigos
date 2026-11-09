import random 
import math
import re
print("====advinhação====")
'''tentativas = []
numero_usuario = int(input("digite um numero para ser advinhado: "))
tentativas.append(numero_usuario)
novo_valor = random.randrange(1, 100, 1)

while True:
    if numero_usuario != novo_valor:
        if numero_usuario > novo_valor:
            print("o valor inserido é maior que o numero escolhido!Tente novamente.")
            numero_usuario = int(input("digite um numero para seradvinhado: "))
            tentativas.append(numero_usuario)
            
        elif numero_usuario < novo_valor:
            print("o valor inserido é menor que o numero escolhido!Tente novamente.")
            numero_usuario = int(input("digite um numero para ser advinhado: "))
            tentativas.append(numero_usuario)
            
    else:
        print("Você acertou o número!")
        print(f"Você levou {len(tentativas)} tentativas, sendo elas: {tentativas}")
        break'''

print("====calculo de areas=====")
escolha_usuário = input("digite qual figura deseja calcular a área (TRI = triangulo, RET = retangulo, QUA = quadrado, TRA = trapézio, LOS = losango, CIR = circulo): ").lower
match escolha_usuário:
    case "tri":
        def area_triangulo(h,b):
            calculo_area = math.prod(h * b) / 2
            return calculo_area
        
        altura = float(input("digite a altura do triangulo: "))
        base = float(input("digite a base do triangulo: "))
        print(f"a area do triangulo é: {area_triangulo(altura,base):.2f}")
    case "ret":
        def area_retangulo(a,b):
            calculo_area = math.prod(a * b)
            return calculo_area
        
        altura = float(input("digite a altura do triangulo: "))
        base = float(input("digite a base do triangulo: "))
        print(f"a area do retangulo é: {area_retangulo(altura,base):.2f}")
    case "qua":
        def area_quadrado(l):
            calculo_area = l ** 2
            return calculo_area
        
        lado = float(input("digite o valor do lado do quadrado: "))
        print(f"a area do quadrado é: {area_quadrado(lado):.2f}")
    case "tra": 
        def area_trapezio(B,b,h):
            calculo_area = math.prod((B + b) * h) / 2
            return calculo_area
        
        base_maior = float(input("digite a base maior do trapezio: "))
        base_menor = float(input("digite a base menor do trapezio: "))
        altura = float(input("digite a altura do trapezio: "))
        print(f"a area do trapezio é: {area_trapezio(base_maior, base_menor, altura):.2f}")
    case "los":
        def area_losango(D, d):
            calculo_area = (math.prod(D,d)) / 2
            return calculo_area
        
        diagonal_maior = float(input("digite a diagonal maior do trapézio: "))
        diagonal_menor = float(input("digite a diagonal menor do trapézio: "))
        print(f"a area do losango é: {area_losango(diagonal_maior, diagonal_menor):.2f}")
    case "cir":
        def area_circulo(r):
            calculo_area = 3,14 * (r ** 2)
            return calculo_area
        
        raio = float(input("digite o raio do circulo: "))
        print(f"a area do circulo é: {area_circulo(raio):.2f}")
    case _:
        print("opção invalida")

print("====calculo de segundo grau====")

def calculo_segundo_grau(a, b, c):
    if a == 0:
        return "O coeficiente 'a' não pode ser zero em uma equação de 2º grau."
        
    delta = (b ** 2) - (4 * a * c)
    
    if delta < 0:
        return "A equação não possui raízes reais (Delta negativo)."
    elif delta == 0:
        x = -b / (2 * a)
        return f"A equação possui uma única raiz real: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"As raízes são: x1 = {x1:.2f} e x2 = {x2:.2f}"
a = float(input("digite o valor de a na equação: "))
b = float(input("digite o valor de b na equação: "))
c = float(input("digite o valor de c na equação: "))
print(calculo_segundo_grau(a, b ,c))
print("====verficiador de senhas====")
import verficiador_de_senha as verif_senha

senha = input("digite a sua senha: ")
print(verif_senha(senha))



