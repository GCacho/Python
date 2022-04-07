#Programa de combate que en 5 turnos tenga que matar un goblin o mueres
#Despues anidar esas sentencias en un loop para acortar el código
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


def ataque_enemigo(): #Es recomendado dejar 2 espacios hacia abajo
    ataque = random.randint(0, 2)
    if ataque == 0: # 0 Representa que fallaste
        print("El enemigo falla el Golpe")
    elif ataque == 1: # 1 Representa que atinaste
        print("El enemigo te atina un golpe")
    elif ataque == 2:
        print("El enemigo te da un golpe crítico")
    return ataque


def nuevo_enemigo(): #Asigna al enemigo nuevo y su vitalidad
    enemigo = random.randint(0, 2)
    if enemigo == 0:
        print ("Te ataca un cerdito")
        vidaenemigo = 2
    elif enemigo == 1:
        print ("Te ataca un Goblin")
        vidaenemigo = 3
    elif enemigo == 2:
        print ("Te ataca un Dragón")
        vidaenemigo = 5
    return vidaenemigo


def daño_a_enemigo(poderataque, salud_enemigo):
    if poderataque == 1:
        salud_enemigo -= 1
        print("El enemigo queda con " + str(salud_enemigo) + " puntos de salud")
    elif poderataque == 2:
        salud_enemigo -= 2
        print("El enemigo queda con " + str(salud_enemigo) + " puntos de salud")
    else:
        print("El enemigo queda con " + str(salud_enemigo) + " puntos de salud")
    return salud_enemigo


def daño_enemigo(poderataque, salud):
    if poderataque == 1:
        salud -= 1
        print("Quedas con " + str(salud) + " puntos de salud")
    elif poderataque == 2:
        salud -= 2
        print("Quedas con " + str(salud) + " puntos de salud")
    else:
        print("Quedas con " + str(salud) + " puntos de salud")
    return salud    


def bloque_combate():  #Montar todo esto dentro de run primero y luego mandarlo a bloque_combate()
    # Primer enemigo
    print("---------------------------------------------")
    salud_enemigo = nuevo_enemigo()     #Aparece el nuevo enemigo y le asigna su salud
    salud_inicial = 5                   #La vitalidad de tu personaje
    print("---------------------------------------------")
    print("Salud del enemigo = " + str(salud_enemigo))
    print("Salud de tu personaje = " + str(salud_inicial))
    sleep(5)
    print("---------------------------------------------")
    print("-------------Inicia El Combate---------------")
    print("---------------------------------------------")
    #for i in range(10): #El combate durará 10 turnos o hasta que alguien muera por la función break
    while salud_enemigo >=0 and salud_inicial >= 0: #tambien lo podemos orillar a infinito ya que cortaremos el bucle con un break
        poder = poder_ataque() #Atacamos al enemigo y definimos el poder del golpe
        salud_enemigo = daño_a_enemigo(poder, salud_enemigo) #Atacamos al enemigo dependiendo del poder se le resta la salud al enemigo y se guarda en la variable la salud con la que quedó el enemigo
        print("---------------------------------------------")
        if salud_enemigo <= 0:
            sleep(5)
            print("Felicidades, venciste a tu enemigo!")
            break
        if salud_inicial <= 0:
            sleep(5)
            print("Te moriste")
            break
        sleep(5)
        poder_enemigo = ataque_enemigo() #El enemigo te ataca y definimos el poder del golpe
        salud_inicial = daño_enemigo(poder_enemigo, salud_inicial) #El enemigo te ataca dependiendo del poder y se te resta la salud dependiendo de la salud inicial asignada
        print("---------------------------------------------")
        sleep(5)
        if salud_enemigo <= 0:
            sleep(5)
            print("Felicidades, venciste a tu enemigo!")
            break
        if salud_inicial <= 0:
            sleep(5)
            print("Te moriste")
            break
    return salud_inicial


def run():  
    salud_personaje = bloque_combate()
    sleep(5)
    print("---------------------------------------------")
    print("Tu personaje queda con " + str(salud_personaje) + " puntos de salud")
    print("---------------------------------------------")

if __name__ == '__main__': #Buenas prácticas de programación
    run()