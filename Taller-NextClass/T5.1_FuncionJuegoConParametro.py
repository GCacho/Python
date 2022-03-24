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
        print("\nTu personaje Lanza una banana a su adversario")
    elif opcion == 2:
        print("\nTu personaje Ataca con un cuchillo a su adversario")
    elif opcion == 3:
        print("\nTu personaje Ataca con una espada a su adversario")   
    else:
        print("\nAl no elegir nada decides pelear con los puños")
#---------------------------------Fin Funciones y parámetros--------------------------------

#---------------------------------Inicio Juego---------------------------------
os.system("cls")
print("""
---------------------------------------------------------
Aparece un goblin salvaje que te quiere agarrar a hostias
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