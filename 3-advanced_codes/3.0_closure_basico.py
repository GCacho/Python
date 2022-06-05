#Los closures son valores de scope superiores que son recordados.

def main():

    a = 1

    def nested():
        print(a)

    return nested

my_func = main()
my_func() #Se puede convertir en función porque heredo los datos de una función anidada

del(main) #Eliminamos la funcion superior pero como ya fue almacenada en my_func no debería de afectar la línea de abajo.

my_func() #Y seguirá funcionando sin importar que la función que recuerda las variables es eliminada.
