#Función con parámetros
#Programa para elegir la habilidad que utilizará un personaje en un videojuego

#---------------------------------Inicio Funciones y Parámetros--------------------------------
import os
from time import sleep


def apelear():
    menu = """
--------------------------------------------------------------
Tu personaje entra en modo de combate, ¿Qué decides hacer a continuación?
1 - Banana
2 - Cuchillo
3 - Espada
--------------------------------------------------------------

Elige una opción: 
---->"""

    opcion = int(input(menu))

    if opcion == 1:
        accion("Lanza una banana ")
    elif opcion == 2:
        accion("Ataca con un cuchillo")
    elif opcion == 3:
        accion("Ataca con una espada")   
    else:
        print("Al no elegir nada decides pelear con los puños")

def accion(habilidad):
    print("----------------------------------------------")
    print("Tu personaje " + habilidad + " a su adversario")
    print("----------------------------------------------")
#---------------------------------Fin Funciones y parámetros--------------------------------

#---------------------------------Inicio Juego---------------------------------
os.system("cls")
print("""
---------------------------------------------------------
Aparece Goblin Salvaje con sed de sangre
---------------------------------------------------------""")
sleep(3)
apelear()
sleep(3)
os.system("cls")
print("""
---------------------------------------------------------
Aparece un Demonio salvaje que te quiere agarrar a besitos
---------------------------------------------------------""")
sleep(3)
apelear()
#---------------------------------Fin Juego------------------------------------