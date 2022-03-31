#Divide y conquista
#El problema se divide en 2 con cada iteración
#¿Cuál es el peor caso?

import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}') #print statement que te da pistas sobre como va corriendo el algoritmo
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2 # // es division de enteros (remueve los decimales)

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


if __name__ == '__main__': #Sirve para importar modulos.
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)]) #Sorted es una funcion que ordena la lista

    encontrado = busqueda_binaria(lista,0,len(lista),objetivo)

    print(lista)
    print(f'El elemento {objetivo} {" esta" if encontrado else "no esta"} en la lista')
