def decorador(func):
    def envoltura(): #wrapper()
        print("Esto se añade a mi función original")
        func()
    return envoltura #wrapper


@decorador #Azucar sintactica, es el decorador básico pero arreglado
def saludo(): 
    print("Hola!")

saludo()