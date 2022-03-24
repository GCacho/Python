class A():
    def __init__(self):
        self.contador = 0
    
    def incrementar(self):
        self.contador += 1
    
    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self._contador = 0 #El __ es para encapsular que es para que solo se pueda ejecutar dentro de la misma clase solamente
    
    def incrementar(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador

print("Objeto 1")

a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador) #Mala practica de programacion

print("Objeto 2")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
print(b._contador)