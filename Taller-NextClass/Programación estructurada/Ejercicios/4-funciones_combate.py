import random
from time import sleep
#----------------Diccionarios--------------------

atacar = {
    0 : "Fallido",
    1 : "Basico",
    2 : "Critico",
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
    

if __name__ == '__main__':
    enemigo = nuevo_enemigo()
    print(f"Aparece un {enemigo} frente a ti. \n{enemigo} te ataca y te encesta un Golpe {nuevo_ataque()}")
    
