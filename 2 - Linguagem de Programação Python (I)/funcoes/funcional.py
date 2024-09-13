# def soma(x,y):
#     return x + y

# def mult(x,y):
#     return x * y
    
# somar = soma
# x=1
# y=2

# def op_aritmetica(fn, op1, op2):
#     return fn(op1,op2)
 
    
# print("A soma de x e y e: ", op_aritmetica(somar,x,y))

# def soma_parcial(a):
#    def concluir_soma(b):
#       return a+b
#    return concluir_soma

# fn = soma_parcial(10)
# print(fn(12))

#ou fn = soma_parcial(10)(12)


def pipeline(transformacoes):
    def processar(texto):
        for transformacao in transformacoes:
            texto = transformacao(texto)
        return texto
    return processar
 
def remover_espacos(texto):
    return texto.replace(" ", "")

def para_minusculas(texto):
    return texto.lower()

def remover_pontuacao(texto):
    import string
    return texto.translate(str.maketrans('', '', string.punctuation))

def inverter_texto(texto):
    return texto[::-1]

transformacoes = [
    remover_espacos,
    para_minusculas,
    remover_pontuacao,
    inverter_texto
]

processar_texto = pipeline(transformacoes)
texto_original = "Hello, World!"
texto_processado = processar_texto(texto_original)
print(texto_processado) 