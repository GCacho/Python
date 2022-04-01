#Crear un pequeño juego donde al 
#Usuario le pregunten por un numero del 1 al 100
#El algoritmo dará pistas para saber si es un número 
#Más grande o más pequeño a la selección del usuario

#Al finalizar subir tu código con tu nombre 
#Al padlet del taller

#Necesitarán de la función Random, int input y un bucle 
#While para llevar a cabo el programa
import random

def run():

    
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("Elige un número entre el 1 y 100\n---->"))
    contador = 0
    while numero_elegido != numero_aleatorio: #== !=
        contador = contador + 1
        if numero_elegido < numero_aleatorio:
            print("-----------------------")
            print("Busca un número más GRANDE")
        else:
            print("-----------------------")
            print("Busca un número más PEQUEÑO")

        print("Llevas: " + str(contador) + " intentos")
        print("-----------------------")
        numero_elegido = int(input("Elige otro número:\n----> "))
    print("Felicidades Ganaste!")


if __name__ == '__main__':
    run()
