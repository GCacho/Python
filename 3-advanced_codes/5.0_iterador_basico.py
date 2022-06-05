# Creando un iterador

my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

# Iterando un iterador

while True:
    try:
        element = next(my_iter)
        print(element)              #Intenta imprimir elementos hasta que ya no queden.
    except StopIteration:           #Stop Iteration es para detener el ciclo si se terminan los elementos o manda un error.
        break

# Cuando no quedan datos, la excepción StopIteration es elevada