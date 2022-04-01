#Programa que te ayuda a elegir un camino - De momento parece que no hace nada especial pero ayuda a disminuir el código

def run(): #Buenas prácticas de programación para correr correctamente un sistema
    import os
    import random
    from time import sleep


    def ataque():
        ataque = random.randint(0, 1) 
        if(ataque==0):
            print("Fallaste el golpe")
        elif(ataque==1):
            print("Golpeas a tu adversario")
        return(ataque)

    #Inicia programa
    poder_golpe=ataque()
    #print(poder_golpe)

    if poder_golpe == 0:
        print("Mueres")
    elif poder_golpe == 1:
        print("Sobrevives")


if __name__ == '__main__': #Se complementa con def run() para inicializar el programa con buenas prácticas de programación
    run()
