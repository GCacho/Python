from ssl import DER_cert_to_PEM_cert

#Pequeño programa que escriba del 1 al 50

def run():
    LIMITE = 50
    contador = 0
    while contador <= LIMITE:
        print('Numero ' + str(contador))
        contador += 5
        

if __name__ == '__main__':
    run()

#Hacer programa que recorra numeros del 1 al 100 solo mostrando los pares

#Hacer programa que recorra numeros del 1 al 100 solo mostrando los impares