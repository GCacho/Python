#Programa que te ayuda a elegir un camino - De momento parece que no hace nada especial pero ayuda a disminuir el código
def camino(trip):
    if(trip==1):
        print("Elegiste seguir derecho")
    elif(trip==2):
        print("Elegiste girar a la derecha")
    elif(trip==3):
        print("Elegiste girar a la izquierda")

opcion = int(input('Elige un camino:\n(1 - Seguir Derecho | 2 - Ir a la Izquierda | 3 - Ir a la derecha:\n--->'))

camino(opcion)
