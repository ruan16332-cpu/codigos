'''import calendar
ano = int(input('digite um ano: '))
mes = int(input('digite um mes: '))

print('\n', calendar.month(ano,mes))'''   

'''numeros = []
while True:
    usuario = float(input('digite um numero '))
    continuar = input("digite 's' para parar e 'n' para continuar: ")
    numeros.append(usuario)
    if continuar == "s":
        break
    
numeros.sort()
print(f"os numeros que o usuario digitou em ordem crescente são: {numeros}")
numeros.reverse()
print(f'os numeros que o usuario digitou em orgem decrescente são: {numeros}')
print(f'o maior numero digitado pelo usuario foi: {max(numeros)}')
print(f'o menor numero digitado pelo usuario foi: {min(numeros)}')'''

def calculo_fatorial(x):
    if x == 0 or x == 1:
        return 1
    return x * calculo_fatorial(x - 1)

num = int(input("digite um numero para calcular seu fatorial: "))
print(calculo_fatorial(num))

