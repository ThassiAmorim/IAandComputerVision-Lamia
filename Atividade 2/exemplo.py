from functools import reduce


class Produto:
    def __init__(self, nome, preco, categoria): #construtor de Produto
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def __repr__(self): # metodo para mostrar as caracteristicas do Produto
        return f"nome={self.nome}, preco={self.preco}, categoria={self.categoria}"
    
    def __str__(self):
        return f"Nome: {self.nome}, Preco: {self.preco}, Categoria: {self.categoria}"

# funcao para adicionar produtos a uma lista chamada inventario
def adicionar_produto(inventario, *args):
    for p in args:
        produto = Produto(p['nome'], p['preco'], p['categoria'])
        inventario.append(produto)

# funcao para calcular a soma cumulativa de inventario utilizando reduce e a lambda
def calcular_valor_total(inventario):
    return reduce(lambda total, produto: total + produto.preco, inventario, 0)  

# funcao utilizando filter para filtrar os produtos por categoria
def filtrar_por_categoria(inventario, categoria):
    return list(filter(lambda produto: produto.categoria == categoria, inventario))

# funcao para mapear um lambda em uma nova lista de descontos
def aplicar_desconto(inventario, desconto):
    return list(map(lambda produto: Produto(produto.nome, produto.preco * (1 - desconto), produto.categoria), inventario))

def exibir_inventario(inventario):
    return [str(produto) for produto in inventario]


def main():
    inventario = []

    adicionar_produto(inventario,
                    {"nome": "Camiseta", "preco": 50.0, "categoria": "Roupas"},
                    {"nome": "Calca", "preco": 80.0, "categoria": "Roupas"},
                    {"nome": "Tenis", "preco": 120.0, "categoria": "Calcados"},
                    {"nome": "Bone", "preco": 30.0, "categoria": "Acessorios"}
    )
                      
    
    inventario_exibicao = exibir_inventario(inventario)
    print("\nInventario:")
    for item in inventario_exibicao:
        print(item)
    valor_total = calcular_valor_total(inventario)
    print(f"Valor total do inventario: R$ {valor_total:.2f}\n")

    roupas = filtrar_por_categoria(inventario, "Roupas")
    print(f"Produtos na categoria 'Roupas': {roupas}\n")

    inventario_com_desconto = aplicar_desconto(inventario, 0.1)
    print("Inventario com desconto:")
    for produto in inventario_com_desconto:
        print(produto)


if __name__ == "__main__":
    main()
