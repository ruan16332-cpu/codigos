coisas = {
    "nome": 'Maria',
    "idade": 21,
    "email": 'maria@gmail.com'
    
}
print(coisas )
print()

lista = {
    "frutas": ['maçã', 'banana', 'laranja', 'melancia'],
    "equipamentos": [["radio", 300],
                     ["tv", 3000],
                     ["cafeteira", 2000]]

}
print(lista['frutas'])
print()
print(lista['frutas'][1])
print()
print(lista['equipamentos'])
print()
def valor_total(x):
    total = 0
    for valor in x:
        total += valor[1]
    return total
print(valor_total(lista['equipamentos']))
print()

def maior_valor(x):
    maior_nome = x[0][0]
    maior_preco = x[0][1]
    for i in x:
        if i[1] > maior_preco:
            maior_preco = i[1]
            maior_nome = i[0]
    return f'{maior_nome}: {maior_preco}'
print(maior_valor(lista['equipamentos']))
print()
lista['eletronicos'] = lista.pop("equipamentos")
print(lista)
print()


