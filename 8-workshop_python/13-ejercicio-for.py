#Crea un programa donde se le pida al usuario que 
#elija un vehículo de un listado, una vez seleccionado,
#imprimir en pantalla el vehículo elegido y preguntar al 
#usuario si quiere volver a elegir o no.
def run():
    for i in range (10000):
        coche = int(input("Selecciona un vehículo:\nPulsa 1: Toyota\nPulsa 2: Audi\nPulsa 3: Batimovil\n------>"))
        if coche == 1:
            print ("Escogiste un Toyota")
        elif coche == 2:
            print ("Escogiste un Audi")
        elif coche == 3:
            print ("Escogiste un Batimovil")
        else:
            print("No te entendí, elige otra vez")
        continuar = int(input("¿Quieres volver a elegir?\nPulsa 1: Si\nPulsa 2: No \n------>"))
        if continuar ==2:
            break


if __name__ == '__main__': #Corre el programa
    run()