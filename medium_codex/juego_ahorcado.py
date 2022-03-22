import random
from random import randint
from select import select

# def lista_palabras():
#     palabra = []
#     with open("./archivos/data.txt", "r", encoding="utf-8") as f:
#         for line in f:
#             palabra.append(line)
#         cantidad_palabras = len(palabra)
#         return cantidad_palabras


def run():
    palabra = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            palabra.append(line) #Se crea absorve la lista de data y se guarda en variable palabra
    
    cantidad_palabras = len(palabra) #Guarda la cantidad de palabras de la lista palabras
    palabra_azar = list(random.choice(palabra)) #Elige una palabra al azar

    ##print(palabra)
    print(palabra_azar)
    print(len(palabra_azar))
    print(cantidad_palabras)

    vidas = 5
    numero_letras = len(palabra_azar) - 1 #Elimina el salto de linea
    blancos = list("-" * numero_letras)
    contador = 0
    correcto = False

    while vidas > 0:
        elect=input("Ingresa una letra:\n---->")
        while contador < numero_letras: #cuenta las letras 
            print(palabra_azar[contador]) #Muestra letra por letra de la lista de palabra_azar
            if palabra_azar[contador] == elect: #Si la letra esta en la palabra 
                letra_correcta = palabra_azar[contador] #Se guarda la letra correcta
                blancos[contador] = letra_correcta
                correcto = True

            contador = contador + 1 #Contador hasta el final
        if correcto == False:
            vidas = vidas - 1

        print(letra_correcta)
        print(blancos)
        print(vidas)
    


if __name__ == "__main__":
    run() 