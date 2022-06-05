from pickle import FALSE


def palindromo(palabra):
    palabra = palabra.replace(' ','') #Hola Como Estas -> HolaComoEstas
    palabra = palabra.lower()         #HolaComoEstas -> holacomoestas
    palabra_invertida = palabra[::-1] #Recorre la palabra o frase de la última letra a la primera
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run(): #Aqui va la parte del código a correr Buenas prácticas de programación
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Si es palindromo')
    else:
        print('No es palindromo')

        
if __name__ == '__main__':
    run()
