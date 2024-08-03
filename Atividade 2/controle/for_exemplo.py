
lista = [1, 2, 3, 4, 5]

for numero in lista:
    print(numero)

#vale lembrar que quando faz enumerate(lista) é possivel obter o indice também e iterar com i

frutas = ['maca', 'banana', 'cereja', 'tomate', 'uva']

for indice, fruta in enumerate(frutas):
    print(f'{indice}, fruta: {fruta}')

for i in range(1,10):
    print(i)