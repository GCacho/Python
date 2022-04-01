def run():
    
    #Programa que permite elegir un arma de una lista.
    #No tiene que ser un videojuego, puede ser una historia con caminos y siruaciones alternativas.

    import random
    from time import sleep
    
    ataque = {
        0 : "Ataque Fallido",
        1 : "Ataque Basico",
        2 : "Ataque Critico",
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

    nuevo_enemigo = random.randint(1, 3) #Elige un nuevo enemigo al azar
    print("--------------------------------------")
    print("Encuentras un: " + str(enemigo[nuevo_enemigo]["tipo"]) + "\nPuntos de salud = " + str(enemigo[nuevo_enemigo]["salud"])) #Nuevo tipo de enemigo
    sleep(5)
    print("--------------------------------------")
    elegir_arma = input("Elige un arma para combatir, Escribe= \n-Banana\n-Espada\n-Lanza\n----->") #Elegir el arma
    personaje["arma"] = elegir_arma #Le asigna el arma al personaje
    print("--------------------------------------")
    print("-----------Inicia el combate----------")
    print("--------------------------------------")
    for i in range(100):
        nuevo_ataque = random.randint(0, 2) #Nuevo tipo de ataque del personaje cada iteracion
        nuevo_ataque_enemigo = random.randint(0, 2) # #Nuevo tipo de ataque del enemigo cada iteracion
        
        #Ataque personaje
        print("Atacas al enemigo = "+ str(ataque[nuevo_ataque]))
        if personaje["arma"] == enemigo[nuevo_enemigo]["debilidad"] :
            print("Tu " + personaje["arma"] + " es la debilidad del " + enemigo[nuevo_enemigo]["tipo"] + " (Daño X 2)")
            enemigo[nuevo_enemigo]["salud"] = enemigo[nuevo_enemigo]["salud"] - nuevo_ataque * 2 #Golpe doble critico debido al tipo de arma
        else:
            enemigo[nuevo_enemigo]["salud"] = enemigo[nuevo_enemigo]["salud"] - nuevo_ataque
        print("Salud del enemigo: " + str(enemigo[nuevo_enemigo]["salud"]))
        if enemigo[nuevo_enemigo]["salud"] <= 0 :
            print("--------------------------------------")
            print(str(enemigo[nuevo_enemigo]["tipo"]) + " Asesinado")
            break
        sleep(3)
        #Ataque enemigo
        print("El enemigo te ataca = "+ str(ataque[nuevo_ataque_enemigo]))
        personaje["salud"] = personaje["salud"] - nuevo_ataque_enemigo
        print("Salud del personaje: " + str(personaje["salud"]))
        if personaje["salud"] <= 0:
            print(str(personaje["salud"]) + " Moriste")
            exit()
        sleep(3)
        
    print("Tu personaje queda con: " + str(personaje["salud"]) + " puntos de salud")


if __name__ == '__main__':
    run()