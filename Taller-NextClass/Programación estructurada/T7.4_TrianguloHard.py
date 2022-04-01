
def run():

    num = int(input("Altura de la pirámide de asteriscos:\n----->")) #Obriene la altura 

    for i in range(num): # i es la iteración que irá incrementando con cada loop - num es el número de veces que se repetirá el loop
        print(' ' * (num - i - 1) + "*" * (2 * i + 1)) 
        # ' ' * (num - i - 1) -> pinta los espacios vacios -> 3 - 0 - 1 = 2 espacios vacios en el primer loop 
        # "*" * (2 * i + 1) -> pinta los asteriscos -> 2 * 0 + 1 = 1 asteriscos en el primer loop

if __name__ == '__main__':
    run()