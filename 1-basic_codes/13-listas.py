
def run():
    print('--------------------------')
    print('-------Objetos-------')
    objetos = ['Hola', 55, False, 3.6]
    print(objetos)
    print('--------------')
    print(objetos[0])
    print('--------------')
    print(objetos[0:2]) #Inicia en el primero y NO toma el último valor
    print('--------------------------')
    objetos.append("Nuevo Elemento")
    print('--------------------------')
    print(f"Listado con el nuevo objeto= {objetos}")
    print('--------------------------')
    print('--------------------------')
    objetos.pop()
    print('--------------------------')
    print(f"Listado con el nuevo objeto borrado= {objetos}")
    print('--------------------------')
    print('-------Números-------')
    numeros = [1, 2, 3, 4, 5]
    numeros2 = [6 ,7 ,8 , 9]
    print(numeros)
    print(numeros2)
    print('--------------------------')
    lista_final = numeros + numeros2
    print(lista_final)
    print('--------------------------')
    print(numeros * 5)
if __name__ == '__main__':
    run()