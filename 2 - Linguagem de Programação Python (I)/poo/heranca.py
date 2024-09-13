class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        return "zzzzz"


class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au!"


animal_generico = Animal("Animal Generico")
meu_cachorro = Cachorro("Rex")

print(animal_generico.emitir_som())  
print(meu_cachorro.emitir_som())  
