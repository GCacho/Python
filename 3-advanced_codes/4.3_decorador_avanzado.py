# Para averiguar cuanto tiempo tarda una función en ejecutarse
from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs): # *args, **kwargs, es para referirnos a que no importa el numero de argumentos que agreguemos, que los acepte
        initial_time = datetime.now()
        func(*args, **kwargs) # Aqui tambien se tienen que agregar ya que es donde se enviarian los parametros 
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre="Guillermo"):
    print("Hola " + nombre)

suma(5, 5)
random_func()
saludo("Guillermo") #Tiene que mostrar el tiempo que se tardaron en ejecutase estas funciones.
