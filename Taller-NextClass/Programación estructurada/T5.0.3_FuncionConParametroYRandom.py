#Programa que te ayuda a elegir un camino - De momento parece que no hace nada especial pero ayuda a disminuir el código

def run(): #Buenas prácticas de programación para correr correctamente un sistema
    import os
    import random
    from time import sleep


    def ataquepj():
        ataque = random.randint(0, 1) 
        if(ataque==0):
            print("Fallaste el golpe")
        elif(ataque==1):
            print("Golpeas a tu adversario")
        return(ataque)
    

    def ataqueenemy():
        ataque = random.randint(0, 1) 
        if(ataque==0):
            print("El rival falla el golpe")
        elif(ataque==1):
            print("El rival te golpea")
        return(ataque)


    #Inicia programa
    poder_golpe=ataquepj()

    if poder_golpe == 0:
        print("Mueres")
        exit()
    elif poder_golpe == 1:
        print("Sobrevives")

    if poder_golpe == 1:
        golpe_enemigo=ataqueenemy()
        if golpe_enemigo == 1:
            print("Mueres")
            exit()
        else:
            print("Sobrevives")

    print("Felicidades Ganaste")


if __name__ == '__main__': #Se complementa con def run() para inicializar el programa con buenas prácticas de programación
    run()
