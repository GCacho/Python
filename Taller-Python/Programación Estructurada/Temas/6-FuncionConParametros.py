#-------------------Inicio de Parametros-------------------
def camino(trip):
    if(trip==1):
        print("El personaje irá derecho")
    elif(trip==2):
        print("El personaje irá a la derecha")
    elif(trip==3):
        print("El personaje irá a la izquierda")
    else:
        print("Diste media vuelta tropezaste y moriste")
        exit()

#-------------------Fin de Parametros-------------------

#-------------------Inicio del Programa -------------------
opcion = int(input("Elige un camino:\n1)Seguir Derecho | 2) Ir a la derecha | 3) Ir a la izquierda \n--->"))
camino(opcion)
opcion = int(input("Elige un camino:\n1)Seguir Derecho | 2) Ir a la derecha | 3) Ir a la izquierda \n--->"))
camino(opcion)
#-------------------Fin del Programa-------------------
