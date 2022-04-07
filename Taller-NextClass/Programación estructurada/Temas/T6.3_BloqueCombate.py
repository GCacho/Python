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


def bloque_combate(salud_inicial):  #Montar todo esto dentro de run primero y luego mandarlo a bloque_combate()
    # Primer enemigo
    print("---------------------------------------------")
    salud_enemigo = nuevo_enemigo()     #Aparece el nuevo enemigo y le asigna su salud
    #salud_inicial = 5                   #Quitamos la vitalidad del bloque y lo importamos de fuera
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
            sleep(5)
            break
        if salud_inicial <= 0:
            sleep(5)
            print("Te moriste")
            break
    return salud_inicial


def run():  
    print("====Nace tu personaje e inicia su aventura con 10 puntos de vida====")
    salud_inicial = 15
    salud_personaje = salud_inicial
    enemigos_eliminados = 0
    print("====Al seguir caminando se percata de que algo lo está acechando====")
    #salud_personaje = bloque_combate(salud_inicial) #Inicia el combate y guarda la vida de tu personaje en una variable
    sleep(5)
    while salud_personaje > 0: #Mientras el personaje siga vivo continua la aventura
        if enemigos_eliminados == 0: #Si es el primer combate entonces...
            salud_personaje = bloque_combate(salud_inicial)
            enemigos_eliminados += 1
            sleep (5)
        else:
            print("---------------------------------------------")
            print("Tu personaje tiene " + str(salud_personaje) + " puntos de salud")
            print("Actualmente llevas " + str(enemigos_eliminados) + " enemigos eliminados")
            print("---------------------------------------------")
            sleep(5)
            continuar = int(input("¿Deseas seguir adelante, volver a casa a descansar o huir de la zona? \nPulsa 1 Para Continuar Luchando!\nPulsa 2 Para Volver a Casa \nPulsa cualquier otra tecla para huir de aquí!\n----->"))
            if continuar == 1:
                salud_personaje = bloque_combate(salud_personaje) #Despues de cada ataque, dar la oportunidad de huir
                enemigos_eliminados += 1
            elif continuar == 2:
                print("Regresas a casa a descansar, recuperas tu salud y pierdes un punto de enemigos eliminados")
                salud_personaje = salud_inicial
                enemigos_eliminados -= 1
                print("---------------------------------------------")
                print("Tu personaje recupera sus " + str(salud_personaje) + " puntos de salud")
                print("Pierdes un enemigo eliminado por lo que actualmente llevas " + str(enemigos_eliminados) + " enemigos eliminados")
                print("---------------------------------------------")
                sleep(5)
            else: 
                print("Huiste de la zona de aventura y recolectas tus victorias")
                print("Lograste escapar con un total de " + str(salud_personaje) + " Puntos de vida")
                print("Asesinaste un total de " + str(enemigos_eliminados) + " Enemigos")
                break

    print("--- XXX Game Over XXX ---")
    exit()

if __name__ == '__main__': #Buenas prácticas de programación
    run()