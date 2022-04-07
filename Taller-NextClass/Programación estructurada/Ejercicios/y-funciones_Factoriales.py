#Escribir una función que reciba un número 
#Entero positivo y devuelva su factorial.

def factorial():
    from math import factorial
    num = int(input("Ingresa el número que desea obtener su factorial: \n----->"))
    if num > 0:
        print(factorial(num))
    else:
        print("El número es negativo, ingrese un número válido.")

if __name__ == '__main__':
    factorial()
