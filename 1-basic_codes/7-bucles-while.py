# def run():
#     LIMITE = 1000 #Si ponemos la variable en mayusculas la convertiriamos en constante
#     contador = 0
#     potencia_2 = 2**contador
#     while potencia_2 < LIMITE:
#         print('2 Elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
#         contador = contador+1
#         potencia_2 = 2**contador

# if __name__ == '__main__':
#     run()

from time import sleep


def run():
    LIMITE = 50
    contador = 0
    while contador < LIMITE:
        print('Numero ' + str(contador+1))
        contador = contador + 1 # Mejor opcion: contador += 1
        sleep(1)

if __name__ == '__main__':
    run()