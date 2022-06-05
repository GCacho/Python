def run():
    mi_diccionario = {
        'id1':1,
        'id2': 2,
        'id3':3,
    }
    print('--------------------------------')

    print(mi_diccionario)

    print('--------------------------------')

    print(mi_diccionario['id1'])
    print(mi_diccionario['id2'])
    print(mi_diccionario['id3'])

    print('--------------------------------')
    print('--------------------------------')

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    #Recorre un tipo de opción 
    for pais in poblacion_paises.keys(): #Método que te devuelve las llaves
        print(pais)

    print('--------------------------------')
    #Recorre un tipo de opción 
    for pais in poblacion_paises.values(): #Método que te devuelve los valores
        print(pais)
    
    #Recorre todas las opciones del diccionario
    print('--------------------------------')

    for pais, poblacion in poblacion_paises.items(): #Método que te devuelve los 2 valores
        print(pais + ' tiene ' + str(poblacion) + ' habitantes ')



if __name__ == "__main__":
    run()