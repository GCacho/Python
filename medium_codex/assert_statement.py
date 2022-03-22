def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0: #Pulsar el visor de bugs en la parte izquierda de visual studio code para recorrer el algoritmo paso a paso
            divisors.append(i) #Con poner un puntito rojo del lado derecho puedes decirle al algoritmo donde detenerse.
    return divisors


def run():
    num = input("Ingresa un numero: ") #Eliminamos el int para que el assert funcione
    assert num.isnumeric(), "Debes ingresar un numero"
    print(divisors(num))
    print("Fin del programa!")

 
if __name__ == "__main__":
    run()