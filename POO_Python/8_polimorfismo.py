#El poliformismo es la habilidad de tomar varias formas
#En python permite cambiar el comportamiento de una superclase para adaptarlo a la subclase

class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando') # --1--


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en mi bicicleta') # --2--

def main():
    persona = Persona('David')
    persona.avanza() #Ando Caminando --1--

    ciclista = Ciclista('Daniel') #Ando moviendome en mi bicicleta --2--
    ciclista.avanza()


if __name__ == '__main__':
    main()
