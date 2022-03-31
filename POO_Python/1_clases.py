
class Coordenada:

    def __init__(self, x, y): #Este es el constructor
        self.x = x 
        self.y = y

    def distancia(self, otra_coordenada): #Formula euclaniana para sacar la diferencia
        x_diff = (self.x - otra_coordenada.x)**2 
        y_diff = (self.y - otra_coordenada.y)**2

        return(x_diff + y_diff)**0.5 #Regresa el total de la distancia entre X y Y


if __name__ == '__main__': #Si este archivo de ejecuta desde la terminal lo podemos correr
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordenada)) #isinstance() funciona para ver si lo que hallamos puesto si es instancia de la classe