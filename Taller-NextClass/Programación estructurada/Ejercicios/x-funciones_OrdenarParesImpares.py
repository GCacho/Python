#Ejercicio 1: Crear un programa que tenga una lista, luego crear una función
#con la cual se van a pedir números al usuario para agregar a la lista.
#Debes crear una segunda función en donde se ordenen los números  
#Pares e impares dentro de dos listas nuevas

lista = []
num = 0

def pedir():
    i = 0 
    cantidad = int(input("¿Cuántos números desea ordenar en la lista? \n----->"))
    while i < cantidad:
        num = int(input("Ingresa un numero: \n---->"))
        lista.append(num)
        i += 1

def ordenar():
    lista.sort() #El método sort() es para ordenar de menor a mayor los datos por default
    pares = []
    impares = []
    for i in lista: #Por cada número en la lista recorrer...
        if i % 2 == 0: #En caso de que el número sea par
            pares.append(i) #append() agrega el número de i al final de la lista
        else: #Em caso de que el número sea impar...
            impares.append(i)
    print(f'Los números pares son: {pares}')
    print(f'Los números impares son: {impares}')  
    
if __name__ == '__main__':
    pedir()
    ordenar()
    print(f'La lista original es: {lista}')