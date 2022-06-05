#Programa que añade mayúsculas.

def mayusculas(func):
    def envoltura(texto): #wrapper()
        return func(texto).upper()
    return envoltura

@mayusculas #Decorador que convierte el texto en mayúsculas.
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje('Cesar'))
