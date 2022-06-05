def run():
    diccionario = {
        1:"Coche",
        2:"Lancha",
        3:"Combi",
    }

    poblacion_paises = {
        "Argentina":45000000,
        "Brasil":212000000,
        "México":128000000,
    }
    
    for pais in poblacion_paises.keys():
        print(pais)

    for pais in poblacion_paises.values():
        print(pais)

    print("-------------------------------")

    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene " + str(poblacion) + " habitantes")

if __name__ == '__main__':
    run()