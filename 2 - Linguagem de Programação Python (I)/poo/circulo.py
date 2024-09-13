class Circulo:

    def __init__(self, raio):
        self.raio = raio


    def calcular_area(self):
        return 3.14159 * self.raio ** 2


    def calcular_perimetro(self):
        return 2 * 3.14159 * self.raio


meu_circulo = Circulo(5)


print("area do circulo:", meu_circulo.calcular_area())


print("Perimetro do circulo:", meu_circulo.calcular_perimetro())
