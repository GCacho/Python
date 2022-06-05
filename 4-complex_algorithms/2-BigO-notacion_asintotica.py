#Crecimiento Asintótico (Conforme crece al infinito)
#No importan varaciones pequeñas
#El enfoque se centra en lo que pasa conforme el tamaño del problema se acerca al infinito
#Mejor de los casos, promedio, peor de los casos
#Big O (ayuda a medir el promedio de los mejores y peores casos posibles)
#Nada más importa el término de mayor tamaño 

#Ley de la suma
def f(n):
    for i in range(n):
        print(i)
    
    for i in range(n):
        print(i)

# 0(n) + 0(n) = 0(n + n) = 0(2n) = 0(n)

#Ley de la suma
def f(n):
    for i in range(n):
        print(i)
    
    for i in range(n * n):
        print(i)

# 0(n) + 0(n) = 0(n * n) = 0(n + n¨2) = 0(n¨2)

#Ley de la multiplicacion
def f(n):
    for i in range(n):
        print(i)
    
        for j in range(n):
            print(i, j)

# 0(n) * 0(n) = 0(n * n) = 0(n¨2)

#Recursividad multiple
def fibonacci(n):

    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# 0(2**n)