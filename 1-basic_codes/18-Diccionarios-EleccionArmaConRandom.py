def run():
    
    #Programa que permite elegir un arma de una lista.
    #No tiene que ser un videojuego, puede ser una historia con caminos y siruaciones alternativas.

    import random
    opcion = random.randint(1, 3)

    arma = {
        "Banana": 1,
        "Espada": 2,
        "Lanza": 3,
    }

    enemigo = {
        1:{
            "tipo" : "Goblin",
            "daño" : 2,
            "salud" : 5,
            "debilidad" : "Espada",
            },
        2:{
            "tipo" : "Dragon",
            "daño" : 5,
            "salud" : 10,
            "debilidad" : "Lanza",
            },
        3:{
            "tipo" : "Gorila",
            "daño" : 3,
            "salud" : 7,
            "debilidad" : "Banana",
            }
    }


    print(enemigo[opcion]["tipo"])

if __name__ == '__main__':
    run()