from functools import reduce

lista = [1==2, 4<=4, 0, 1, False]

verdade = lambda i: i
print(list(filter(verdade, lista)))

alunos = [
    {'nome': 'Ana',     'nota': 8.9},
    {'nome': 'Joao',    'nota': 6.3},
    {'nome': 'Moises',  'nota': 3.8},
    {'nome': 'Altair',  'nota':   7},
    {'nome': 'Zuleide', 'nota': 4.4}
]

aluno_aprovado = lambda aluno: aluno['nota']>=6

alunos_aprovados = list(filter(aluno_aprovado, alunos))

#Ou alunos_aprovados = [aluno for aluno in alunos if aluno['nota']>=6]

print(alunos_aprovados, "\n")

obter_nota = lambda aluno: aluno['nota']
print(obter_nota(alunos[2]))

somar = lambda a,b: a+b

notas_aprovados = map(obter_nota, alunos_aprovados)
print(reduce(somar, notas_aprovados, 0)/len(alunos_aprovados))

#Outro exemplo de lambda
lista = [1==2, 4<=4, 0, 1, False]

verdade = lambda i: i
print(list(filter(verdade, lista)))