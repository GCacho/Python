#Programa que te ayuda a elegir un camino - De momento parece que no hace nada especial pero ayuda a disminuir el código
import random
def camino(trip):
    if(trip==1):
        print("Elegiste seguir derecho")
    elif(trip==2):
        print("Elegiste girar a la derecha")
    elif(trip==3):
        print("Elegiste girar a la izquierda")

opcion = random.randint(1, 3) 
print('Elige un camino:\n(1 - Seguir Derecho | 2 - Ir a la Izquierda | 3 - Ir a la derecha:\n\nNúmero al azar---> ' + str(opcion) + '\n')

camino(opcion)
