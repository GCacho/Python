#Va intercambiando el valor más grnade de la lista hacia la derecha y va copiando y pegando el menor hacia atras para ordenar la lista 
import random

def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
        
    return lista

if __name__ == '__main__': #Sirve para importar modulos.
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)] #Sorted es una funcion que ordena la lista
    print(lista) #lista sin ordenar

    print('-------------------------------------------')

    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada) #lista ordenada