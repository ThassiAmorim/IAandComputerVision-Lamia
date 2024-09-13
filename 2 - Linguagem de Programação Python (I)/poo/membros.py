class Contador:
    cont = 0
    
    def inst(self):
        return "Sou uma instancia"
    
    def inc_self(self):
        self.cont += 1 # como o primeiro valor de self.cont nao existe ele pega da classe, depois passa a ser o dele
        return self.cont
    
    @classmethod
    def inc(c):
        c.cont+=1
        return c.cont
     
    @classmethod
    def dec(c):
        c.cont-=1
        return c.cont
            
            
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec(), "\n") #termina em 2

c = Contador()
print(c.inc_self()) # self.cont pega o valor de 2 e soma com 1 
print(c.inc_self())
print(c.inc_self(), "\n")

print(Contador.inc())# Contador.cont pega o seu valor original de 2 e soma 1
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())