import random
from time import sleep
#----------------Diccionarios--------------------

atacar = {
    0 : "Falla el golpe",
    1 : "Encesta un golpe Básico",
    2 : "Encesta un golpe Crítico",
}

personaje = {
    "salud" : 20,
    "arma" : "", #Se asigna mas adelante
}

enemigo = {
    1:{
        "tipo" : "Gorila",
        "salud" : 5,
        "debilidad" : "Banana",
        },
    2:{
        "tipo" : "Goblin",
        "salud" : 10,
        "debilidad" : "Espada",
        },
    3:{
        "tipo" : "Dragon",
        "salud" : 15,
        "debilidad" : "Lanza",
        }
}

def nuevo_enemigo():
    nuevo_enemigo = random.randint(1, 3) #Elige un nuevo enemigo al azar
    return enemigo[nuevo_enemigo]

def nuevo_ataque():
    nuevo_ataque = random.randint(0, 2)
    return atacar[nuevo_ataque]

def estadisticas_enemigo(enemigo):
    print(f"Aparece un {enemigo['tipo']} frente a ti.\nEl {enemigo['tipo']} tiene {enemigo['salud']} puntos de salud y su debilidad es una {enemigo['debilidad']}")

def ataque_enemigo():
    print(f"{enemigo['tipo']} te ataca y {nuevo_ataque()}")
    

if __name__ == '__main__':
    enemigo = nuevo_enemigo()
    estadisticas_enemigo(enemigo)
    ataque_enemigo()
    