import random
from time import sleep


def poder_ataque():
    ataque = random.randint(0,2)
    if ataque == 0:
        print("Fallaste el golpe")
    elif ataque == 1:
        print("Atinaste un golpe básico")
    elif ataque == 2:
        print("Atinaste un golpe CRÍTICO")
    return ataque


def poder_ataque_enemigo():
    ataque = random.randint(0,2)
    if ataque == 0:
        print("Tu enemigo falló el golpe")
    elif ataque == 1:
        print("Tu enemigo te dio un golpe básico")
    elif ataque == 2:
        print("Tu enemigo te atinó un golpe CRÍTICO")
    return ataque

    
def run():
    ataque = poder_ataque() #Se guarda el valor en la variable e imprime el contenido de la función
    ataque_enemigo = poder_ataque_enemigo()
    print(ataque) #Imprime el valor que se regresó de la función
    print(ataque_enemigo)


if __name__ == '__main__':
    run()