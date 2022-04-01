
class Lavadora:

    def __init__(self):
        self.color="Blanca"
        self.capacidad_carga="10 kg"
        self.tipo="Automática"

    def lavar(self, temperatura):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura): #Con guión bajo significa que es un metodo distinto y privado 
        print(f'Llenando el tanque con agua {temperatura} ')

    def _anadir_jabon(self):
        print('Anadiendo jabon')
    
    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando')

if __name__=='__main__':
    lavadora = Lavadora()
    lavadora.lavar("Fría")
    lavadora._anadir_jabon()
    print(f'Tu lavadora es de color {lavadora.color}')
    lavadora.color="Negra"
    print(f'Tu lavadora ahora es de color {lavadora.color}')

    