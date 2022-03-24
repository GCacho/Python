#Función con parámetros
#Programa para elegir la habilidad que utilizará un personaje en un videojuego

#---------------------------------Inicio Funciones--------------------------------
import os
from time import sleep

def apelear():
    menu = """
--------------------------------------------------------------
Tu personaje va a luchar, ¿Qué decides hacer a continuación?
Atacar con:
1 - Banana
2 - Cuchillo
3 - Espada
--------------------------------------------------------------

Elige una opción: 
---->"""

    opcion = int(input(menu))

    if opcion == 1:
        accion(nombre, "Lanza una banana")
        poder=1

    elif opcion == 2:
        accion(nombre, "Ataca con un cuchillo")
        poder=2
    elif opcion == 3:
        accion(nombre, "Ataca con una espada")   
        poder=3
    else:
        print("Al no elegir nada decides pelear con los puños")
        poder=0
    return poder

def accion(nombre, habilidad):                              #Conecta con apelear() automáticamente
    print(nombre + " " + habilidad + " a su adversario")


#---------------------------------Fin Funciones--------------------------------

#---------------------------------Inicio Juego---------------------------------
#----Elegir nombre---
os.system("cls")
nombre=input("Ingresa el nombre de tu personaje:\n--->")
#---Primer Adversario
import os
print("\nAparece Goblin Salvaje con sed de sangre")
sleep(3)
res = apelear()
if(res==2 or res==3):
    print("Tu ataque funciono! Ganaste")
else:
    print("El arma no tenía suficiente poder, Perdiste")
    exit()
sleep(3)
#Segundo Adversario
os.system("cls")
print("\nAparece araña gigante que te quiere comer vivo")
sleep(3)
if(apelear()==3):
    print("Tu ataque funciono! Ganaste")
else:
    print("El arma no tenía suficiente poder, Perdiste")
    exit()
sleep(3)
#Tercer Adversario
os.system("cls")
print("\nAparece un Gorila gigante gigante que te quiere comer vivo")
sleep(3)
if(apelear()==1):
    print("El gorila gigante se distrae con la banana! Ganaste")
else:
    print("El arma no tenía suficiente poder, Perdiste")
    exit()
# #---------------------------------Fin Juego------------------------------------