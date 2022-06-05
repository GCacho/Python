def decorador(func):
    def envoltura(): #wrapper()
        print("Esto de añade a mi función original")
        func()
    return envoltura #wrapper

def saludo():
    print("Hola!")

saludo()
# Output
# Hola!

print("---------Muestra División------------")

saludo = decorador(saludo)
saludo() #Se le añade el decorador a la función de saludo.
# Output
# Esto se añade a mi fucnión original
# Hola!