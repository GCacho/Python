#Programa de combate
def run():
    import random
    from time import sleep


    def ataque(): #Es recomendado dejar 2 espacios hacia abajo
        ataque = random.randint(0, 1)
        if ataque == 0: # 0 Representa que fallaste
            print("Fallaste el Golpe")
        elif ataque == 1: # 1 Representa que atinaste
            print("Atinaste el Golpe")
        return ataque

        
    #Corre el programa
    poder = ataque()
    sleep(1)
    if poder == 0:
        print("Te moriste, sorry")
        sleep(1)
        print("------Game Over--------")
        sleep(2)
        exit()
    elif poder == 1:
        print("Acabaste con tu enemigo")
        sleep(1)
        print("------Continua el juego------")
        sleep(2)

    poder = ataque()
    sleep(3)

    if poder == 0:
        print("Te moriste, sorry")
        sleep(1)
        print("------Game Over--------")
        sleep(2)
        exit()
    elif poder == 1:
        print("Acabaste con tu enemigo")
        sleep(1)
        print("------Continua el juego------")
        sleep(2)
        print("Sobreviviste Felicidades")
        sleep(1)
        print("------Has ganado-------")
        sleep(2)
        exit()


if __name__ == '__main__': #Buenas prácticas de programación
    run()