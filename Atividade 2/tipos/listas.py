# as listas são arrays em python

lista = [] # para iniciar uma lista vazia
print("lista = []", lista)

lista = [1,2,3] # para iniciar uma lista com valores
print("lista = [1,2,3]", lista)

# para selecionar uma posicao
print("lista[1]", lista[1])

lista.append(94) # para adicionar um elemento a lista
print("lista.append(94)", lista)

lista[0] = 0 # para alterar elementos pela ordem
print("lista[0] = 0", lista)

lista.remove(94) #para remover um elemento da lista 
print("lista.remove(94) ", lista)

len(lista) #para verificar a quantidade de elementos
print("len(lista) ", len(lista))

elemento_ultimo = lista.pop()# remove e retorna o ultimo elemento da lista
elemento_primeiro = lista.pop() #remove e retorna o primeiro elemento
print("elemento_ultimo ", elemento_ultimo)
print("elemento_primeiro ", elemento_primeiro)
print("lista: ",lista)