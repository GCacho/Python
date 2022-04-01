class Rectangulo:

    def __init__(self, base, altura): # --1-- base = lado, altura = lado
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura # --1-- lado * lado
    

class Cuadrado(Rectangulo): #La clase cuadrado extiende al rectangulo

    def __init__(self, lado):
        super().__init__(lado, lado) #Permite obtener una referencia de la superclase "Rectangulo" --1--


if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area()) #12

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area()) #25