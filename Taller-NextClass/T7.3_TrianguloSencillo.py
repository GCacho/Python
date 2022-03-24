from time import sleep

def run():
    lineas = int(input('Numero de lineas:')) 
    for numero_linea in range(lineas): 
        espacios = lineas - numero_linea - 1
        asteriscos = 1 + numero_linea * 2
        print (" " * espacios + "*" * asteriscos)
        sleep(2)

if __name__ == '__main__':
    run()
