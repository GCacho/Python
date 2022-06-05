#Siempre es bueno dejar 2 espacios entre funciones como buena práctica de programación
def palindromo(palabra):
    palabra = palabra.replace(' ','') #Elimina los espacios entre palabras
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1] #Recorre la palabra o frase de la última letra a la primera
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run(): #Buenas prácticas de programación para correr correctamente un sistema
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__': #Se complementa con def run() para inicializar el programa con buenas prácticas de programación
    run()