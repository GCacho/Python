from time import sleep

def run():
    # contador = 0
    # while contador < 5:
    #     print('Numero ' + str(contador+1))
    #     contador += 1
    #     sleep(1)

    for contador in range(5): #Probar tambien range(1, 6) para explicar que todo inicia en 0
        print(contador)
        sleep(1)


if __name__ == '__main__':
    run()