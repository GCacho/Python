#Algoritmo que permite medir la cantidad de tiempo que se tarda el programa en terminar de ejecutarse.
import sys #Sistema de seguridad para evitar loops muy grandes
import time

sys.setrecursionlimit(1000000) #Incrementa el numero de iteraciones posibles (amplia la recursividad)

def factorial(n):
    respuesta = 1

    while n > 1: #Algoritmo que obtiene el factorial de un numero
        respuesta *= n
        n -= 1

    return respuesta

def factorial_recursivo(n):
    if n == 1:
        return 1

    return n * factorial_recursivo(n - 1)


if __name__ == '__main__':
    n = 1000 #No levantar mucho el dato porque windows crashea por el tipo de algoritmo

    comienzo = time.time()
    #print(factorial(n))
    factorial(n)
    final = time.time()
    print(final - comienzo) #Medimos cuanto tarda el programa en ejecutarse

    comienzo = time.time()
    #print(factorial_recursivo(n))
    factorial_recursivo(n)
    final = time.time()
    print(final - comienzo)