#Programa de combate que en 5 turnos tenga que matar un goblin o mueres
#Despues anidar esas sentencias en un loop para acortar el código
def run():
    import random
    from time import sleep


    def poder_ataque(): #Es recomendado dejar 2 espacios hacia abajo
        ataque = random.randint(0, 2)
        if ataque == 0: # 0 Representa que fallaste
            print("Fallaste el Golpe")
        elif ataque == 1: # 1 Representa que atinaste
            print("Atinaste el Golpe")
        elif ataque == 2:
            print("Diste un Golpe Crítico")
        return ataque


    def moriste():
        print("Te moriste, sorry")
        sleep(1)
        print("------Game Over--------")
        sleep(2)
        exit()

    
    def golpe():
        print("Acabaste con tu enemigo")
        sleep(1)
        print("------Continua el juego------")
        sleep(2)

    
    def victoria():
        print("Sobreviviste Felicidades")
        sleep(1)
        print("------Has ganado-------")
        sleep(2)
        exit()


    def nuevo_enemigo():
        enemigo = random.randint(0, 2)
        if enemigo == 0:
            print ("Te ataca cerdito")
            vidaenemigo = 4
        elif enemigo == 1:
            print ("Te ataca un Goblin")
            vidaenemigo = 8
        elif enemigo == 2:
            print ("Te ataca un Dragón")
            vidaenemigo = 10
        return vidaenemigo
    

    def daño_enemigo(poderataque, salud_enemigo):
        if poderataque == 1:
            salud_enemigo -= 1
            print("El enemigo queda con " + str(salud_enemigo) + " puntos de salud")
        elif poderataque == 2:
            salud_enemigo -= 2
            print("El enemigo queda con " + str(salud_enemigo) + " puntos de salud")
        else:
            print("Haz fallado, el enemigo queda con " + str(salud_enemigo) + " puntos de salud")
        return salud_enemigo


        
    #---------------------Corre el programa------------------
    # Primer enemigo
    salud_enemigo = nuevo_enemigo() #Aparece el nuevo enemigo y le asigna su salud
    poder = poder_ataque() #Atacamos al enemigo y definimos el poder del golpe
    salud_enemigo = daño_enemigo(poder, salud_enemigo) #Atacamos al enemigo dependiendo del poder se le resta la salud al enemigo y se guarda en la variable la salud con la que quedó el enemigo
    
    poder = poder_ataque() #Repetimos el ataque con el mismo enemigo
    daño_enemigo(poder, salud_enemigo) #Atacamos al enemigo dependiendo del poder se le resta la salud al enemigo y se guarda en la variable la salud con la que quedó el enemigo
    
    
    
    

    victoria() #Si termina las sentencias ganas
    #---------------------Fin Corre el programa------------------

if __name__ == '__main__': #Buenas prácticas de programación
    run()