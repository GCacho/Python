def suma(n1,n2):
    res = n1 + n2
    return res

def resta(n1,n2):
    res = n1 - n2
    return res

def multiplicar(n1,n2):
    mult = n1 * n2
    return mult
    
def div(n1,n2):
    div = n1 / n2
    return div

if __name__ == '__main__':
    operacion = int(input("¿Qué operación quieres realizar?\nPulsa:\n1)Suma\n2)Resta\n3)Multiplicación\n4)División\n---->"))
    n1 = int(input("Ingrese el primer número a calcular: "))
    n2 = int(input("Ingrese el segundo número a calcular: "))
    if operacion == 1:
        print(suma(n1,n2))
    elif operacion == 2:
        print(resta(n1,n2))
    elif operacion == 3:
        print(multiplicar(n1,n2))
    elif operacion == 4:
        print(div(n1,n2))
    else:
        print("¡Ingresa un valor válido por favor!")