def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0: #Pulsar el visor de bugs en la parte izquierda de visual studio code para recorrer el algoritmo paso a paso
            divisors.append(i) #Con poner un puntito rojo del lado derecho puedes decirle al algoritmo donde detenerse.
    return divisors


def run():
    try: #Manejo de excepciones
        num = int(input("Ingresa un numero!"))
        print(divisors(num))
        print("Fin del programa!")
    except ValueError: #Manejo de excepciones / ValueError porque era un error de tipo value
        print("Debes ingresar un número: ")

 
if __name__ == "__main__":
    run()