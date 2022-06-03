from tkinter import N


def my_gen():

    print("Hola mundo!")
    n = 0 
    yield n #Es lo mismo que return pero en vez de terminar la funcion la pausa

    print("Hola cielo!")
    n = 1 
    yield n 

    print("Hola infierno!")
    n = 2 
    yield n 

a = my_gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
