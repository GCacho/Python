import random


def generar_constrasena():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    CARACTERES = MAYUS + MINUS + NUMS + CHARS
    contrasena = []

    for i in range(15):
        caracter_random = random.choice(CARACTERES) #random.choice() elige un caracter al azar 
        contrasena.append(caracter_random) #append() agrega el caracter creado al azar a la lista contrasena
    
    contrasena = "".join(contrasena) #Hack para convertir una lista en un string
    return contrasena #Regresa la lista en formato de string

def run():
    contrasena = generar_constrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    run()