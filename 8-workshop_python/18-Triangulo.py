def run():
    num = int(input("Altura de la pirámide de asteriscos:\n----->")) #Obtiene la altura 

    for i in range(num):
        print(' ' * (num - i - 1) + "*" * (2 * i * 1) )

if __name__ == '__main__':
    run()