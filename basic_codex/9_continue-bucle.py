def run():
    for contador in range(1000):
        if contador % 2 != 0: 
            continue #Se salta la vuelta del ciclo y no se imprime ninguna línea de abajo en este caso los números impares
        print(contador)

if __name__ == '__main__':
    run()