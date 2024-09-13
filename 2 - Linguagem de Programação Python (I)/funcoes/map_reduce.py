from functools import reduce
from basico import somar

def somar_nota(delta):
    def calc(nota):
        return nota+delta
    return calc


notas = [6.4, 7.2, 5.8, 8.4]
notas_atualizadas = list(map(somar_nota(1.6), notas))

print(notas_atualizadas)

total = reduce(somar, notas, 0)
print(total)

# Outro exemplo de map
numeros = [1, 2, 3, 4, 5] 
def quadrado(x):
    return x * x

numeros_quadrados = list(map(quadrado, numeros))

print(numeros_quadrados)