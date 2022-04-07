def suma(n1, n2):
    return print(f'La suma de {n1} + {n2} es : {n1 + n2}')

def resta(n1, n2):
    return print(f'La resta de {n1} - {n2} es : {n1 - n2}')

def multiplicacion(n1, n2):
    return print(f'La multiplicación de {n1} x {n2} es : {n1 * n2}')

def division(n1, n2):
    return print(f'La suma de {n1} ÷ {n2} es : {n1 / n2}')
    

if __name__ == '__main__':
    operacion = int(input("¿Qué operación desea realizar? \nPulse:\n1)Suma\n2)Resta\n4)Multiplicación\n5)División\n------>"))
    num1 = int(input("Ingrese el primer número a calcular: \n----->"))
    num2 = int(input("Ingrese el segundo número a calcular: \n----->"))
    
    if operacion == 1:
        suma(num1, num2)
    elif operacion == 2:
        resta(num1, num2)
    elif operacion == 3:
        multiplicacion(num1, num2)
    elif operacion == 4:
        division(num1, num2)
    else:
        print("¡Ingrese un dato válido!")