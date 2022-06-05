
def divide_elementos_de_lista(lista, divisor):
    try: #intenta el codigo
        return [i / divisor for i in lista]
    except ZeroDivisionError as e: #Mandas a llamar las excepciones en este caso ZeroDicisionError y las evitas  
        print(e)
        return lista

lista = list(range(10))
divisor = 0 #si ponemos 0 intenta dividir entre cero mandando un error, con el try arriba lo capturamos y evitamos el bug

print(divide_elementos_de_lista(lista, divisor))
