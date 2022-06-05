def run():
    
    #Programa que permite elegir un arma de una lista.
    #No tiene que ser un videojuego, puede ser una historia con caminos y siruaciones alternativas.

    arma = {
        "Banana": 1,
        "Espada": 2,
        "Lanza": 3,
    }

    enemigo = {
        "Goblin":{
            "daño" : 2,
            "salud" : 5,
            "debilidad" : "Espada",
            }
    }

    print(enemigo["Goblin"]["daño"])

if __name__ == '__main__':
    run()