import random
from time import sleep
#----------------Diccionarios--------------------


personaje = {
    "salud" : 20,
    "arma" : "Espada", #Se asigna más adelante
    "rango_damage" : 10, #Se asigna el random en el combate
    "damage" : 0
}

enemigo = {
    1:{
        "tipo" : "Gorila",
        "salud" : 5,
        "debilidad" : "Banana",
        "rango_damage" : 2,
        "damage" : 0
        },
    2:{
        "tipo" : "Goblin",
        "salud" : 10,
        "debilidad" : "Espada",
        "rango_damage" : 5,
        "damage" : 0
        },
    3:{
        "tipo" : "Dragon",
        "salud" : 15,
        "debilidad" : "Lanza",
        "rango_damage" : 10,
        "damage" : 0
        }
}


def nuevo_enemigo():
    nuevo_enemigo = random.randint(1, 3) #Elige un nuevo enemigo al azar
    return enemigo[nuevo_enemigo]


def estadisticas_enemigo(enemigo):
    print(f"El {enemigo['tipo']} tiene {enemigo['salud']} puntos de salud y su debilidad es una {enemigo['debilidad']}")


def ataque_enemigo(enemigo):
    print(f"El {enemigo['tipo']} te ataca y te hace {enemigo['damage']} puntos de daño")
    personaje["salud"] = personaje["salud"] - enemigo["damage"]  #Regresa el daño que produce el enemigo.


def ataque(enemigo, personaje):
    print(f"Cargas contra el enemigo y le haces {personaje['damage']} de daño")
    if personaje["arma"] == enemigo["debilidad"]:
        print(f"Tu {personaje['arma']} es la debilidad del {enemigo['tipo']} por lo que haces el doble de daño")
        enemigo["salud"] = enemigo["salud"] - (personaje["damage"] * 2)
    else:
        enemigo["salud"] = enemigo["salud"] - personaje["damage"]


def estadisticas_personaje(personaje):
    print(f"Tu personaje tiene {personaje['salud']} puntos de salud y tienes una {personaje['arma']} como arma")


def combate():
    enemigo = nuevo_enemigo()    
    print(f"Aparece un {enemigo['tipo']} frente a ti")                              #Crea un nuevo enemigo y lo muestra
    while enemigo["salud"] > 0 and personaje["salud"] > 0:
        personaje["damage"] = random.randint(0, personaje["rango_damage"])          #Se asigna el valor con los parametros asignados en los personajes
        enemigo["damage"] = random.randint(0, enemigo["rango_damage"])
        estadisticas_personaje(personaje)                                           #Muestra las estadisticas del personaje.
        estadisticas_enemigo(enemigo)                                               #Muestra las estadisticas del enemigo
        ataque_enemigo(enemigo)                                                     #Muestra y registra el ataque del enemigo / disminuye la salud del personaje de ser necesario
        print(f"Tu personaje queda con {personaje['salud']} puntos de salud")
        ataque(enemigo, personaje)                                                  #Muestra las estadisticas del enemigo
        print("-----------------------------------------------")
        sleep(10)

    estadisticas_personaje(personaje)                                           #Muestra las estadisticas del personaje.
    estadisticas_enemigo(enemigo) 
    
if __name__ == '__main__':
    combate()
    