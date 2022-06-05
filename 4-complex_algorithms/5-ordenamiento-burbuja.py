#El ordenamiento de burbuja es un algoritmo que recorre repetidamente una lista que necesita ordenarse.
#Compara elementos adyacentes y los intercambia si están en el orden incorrecto.
#Este procedimiento se repite hasta que no se requieren más intercambios,
#Lo que indica que la lista se encuentra ordenada.

import random

def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n): #recorrer varias veces la lista
        for j in range(0, n - i - 1): #Para ya no recorrer lo recorrido (no tan buen algoritmo)

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #Intercambiamos los elementos

    return lista

if __name__ == '__main__': #Sirve para importar modulos.
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)] #Sorted es una funcion que ordena la lista
    print(lista) #lista sin ordenar

    print('-------------------------------------------')

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada) #lista ordenada
