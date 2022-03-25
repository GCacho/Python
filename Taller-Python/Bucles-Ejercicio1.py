def run():
    numero = int(input("Ingresa un numero"))
    for contador in range(1,11): # contador avanzará de uno en uno hasta llegar al rango 51
        print(str(contador), ' X ' , str(numero) , str(contador*numero))  

if __name__ == '__main__':
    run()