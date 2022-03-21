import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    contador = 0
    while numero_elegido != numero_aleatorio:
        contador = contador + 1
        if numero_elegido < numero_aleatorio: 
            print('----------------------------')
            print('Busca un numero mas GRANDE')
        else:
            print('----------------------------')
            print('Busca un numero mas PEQUEÑO')
        print("Llevas: " + str(contador) + " intentos")
        print('----------------------------')
        numero_elegido = int(input('Elige otro numero: '))
    print('Ganaste')
    

if __name__ == '__main__':
    run()