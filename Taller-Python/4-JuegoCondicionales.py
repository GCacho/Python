from select import select
from time import sleep

skull = ("""
                        _____
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
""")

print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("------------------La Isla Maldita------------------")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(skull)
sleep(2)
print("----------Crea a tu Personaje----------")
nombre = input("Elije un nombre: ")
print("\n----------Elige un Arma----------")

arma = int(input("--Pulsa 1-- Para elegir una Espada \n--Pulsa 2-- Para elegir una Banana \n--Pulsa cualquier otra tecla-- para continuar sin arma \n\nElige ----> "))
if arma == 1:
    arma = "Espada"
elif arma == 2:
    arma = "Banana"
else:
    arma = "piedrita que no sirve para nada"

print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("¡Hola " + nombre + " bienvenido a la isla maldita!")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
sleep(2)
print("---------------------------------------")
print("Tuviste un su6eño extraño y al despertar te percatas \nde que ya no estas en casa, ni recuerdas como \nes que llegaste a este lugar...")
print("---------------------------------------")
sleep(7)
print("Miras a tu alrededor y te das cuenta de que\nHas encontrado una " + arma )
print("---------------------------------------")
sleep(5)
print("Procedes a guardarla en tu bolsillo")
print("---------------------------------------")
sleep(5)
print("Volteas a los alrededores confundido")
print("---------------------------------------")
sleep(5)
print("Despues de caminar unos minutos te encuentras\ncon una intersección que muestra un letrero con el siguiente mensaje:")
print("---------------------------------------")
sleep(8)
print("¡Bienvenidos aventureros a la isla maldita!\n¡Abandonad toda esperanza pues nadie sale vivo de aqui!")
print("---------------------------------------")
sleep(8)
print("Notas que hay 2 letreros mostrando 2 caminos distintos \nEl primero dice --Volcan Activo--\nEl segundo dice --Ciudad de los monos Asesinos--")
print("---------------------------------------")
sleep(10)
print("---Elige un camino para poder continuar---")
camino = int(input("--Pulsa 1-- Para ir por el volcán \n--Pulsa 2-- Para ir por la cabaña de los monos asesinos \n--Pulsa cualquier otra tecla-- Para quedarte en el mismo lugar \nElige ----> "))

print("---------------------------------------")
if camino == 1:
    print("Elegiste ir por el camino del volcán activo")
    print("---------------------------------------")
    sleep(5)
    print("Al ir avanzando te encuentras con un puente colgante que atravieza la lava")
    print("---------------------------------------")
    sleep(5)
    print("Al examinar la situación caes en cuenta de que puedes \ncruzar el lago de lava a través de un costado del volcán por un angosto camino de piedras")
    print("---------------------------------------")
    sleep(7)
    print("\n---Elige un camino para poder continuar---\n")
    volcan = int(input("--Pulsa 1-- Para ir por el puente colgante \n--Pulsa 2-- Para cruzar por el camino de piedras \n--Pulsa cualquier otra tecla-- Para saltar a la lava \nElige ----> "))
    if volcan == 1:
        print(nombre + " Elige cruzar por el puente colgante")
        print("---------------------------------------")
        sleep(5)
        print("A mitad del camino el puente cede por el peso dejando a " + nombre + " en caida libre")
        sleep(5)
        print(nombre + " muere cocinado en la lava.")
        print("---------------------------------------")
        print("---------------GAME OVER-------------------")
        print("---------------------------------------")
        exit()
    elif volcan==2:
        print(nombre + " Elige cruzar por el camino de piedras")
        print("---------------------------------------")
        sleep(5)
        print("A mitad del camino " + nombre + " ¡Encuentra un grupo de Goblins hambrientos!")
        sleep(5)
        print("---------------------------------------")
        if arma == "Espada":
            print(nombre + " Saca su " + arma + " y asesina a los goblins abriendose paso hasta la salida")
            print("---------------------------------------")
            sleep(5)
            print("¡Felicidades " + nombre + " haz sobrevivido a la isla maldita!")
        else:
            print(nombre + " Saca su " + arma)
            print("---------------------------------------")
            sleep(5)
            print("Los goblins con una sonrisa en la cara brincan sobre\n" + nombre + " Acabando con su miserable vida")
            print("---------------------------------------")
            sleep(5)
    else:
        print(nombre + " Elige saltar al lago de lava y terminar con su miserable vida")
        print("---------------------------------------")
        print("---------------GAME OVER-------------------")
        print("---------------------------------------")
        exit()
elif camino==2:
    print("Elegiste ir por la cabaña de los monos asesinos")
    print("---------------------------------------")
else: 
    print("Elegiste quedarte donde estas parado actualmente\nTe quedas sentado junto al letrero, esperando a decidir\nCuando de repente de los arbustos salen unas\ncalaveras malditas y acaban con tu miserable vida")
    print("---------------GAME OVER-------------------")
    print("---------------------------------------")
    exit()
