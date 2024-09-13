# tuplas são listas imutaveis

tupla = (50, 34, 23)

# Para definir tuplas de um elemento, utilizar virgula para que não se confunda com outros tupos de dados

tupla = (20,)
print("Tupla vazia: ", tupla, "do tipo: ", type(tupla))

# Caso precise alterar uma tupla deve-se criar outra 
nova_tupla = tuple(list(tupla)+[86])
print("Nova tupla: ", nova_tupla)

