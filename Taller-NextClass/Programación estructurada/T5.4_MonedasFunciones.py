#Las funciones fueron creadas para acortar código que se repite cambiando pocos parámetros a través de "Bloques" de código.
#Programa que calcula el valor de dolares a pesos con funciones para acortar el código
#Guarda el menú en la variable opción

def conversor(tipopeso, valordolar):
    pesos = input("¿Cuántos pesos " + tipopeso + " tienes?\n--->")   
    pesos = float(pesos) 
    valor_dolar = valordolar
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)     
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 🪙

1 - Pesos mexicanos
2 - Pesos argentinos
3 - Pesos colombianos 

Elige una opción: """
opcion = int(input(menu))

if opcion == 1:
    conversor("Mexicanos", 20.05)

elif opcion == 2:
    conversor("Argentinos", 103.85)

elif opcion == 3:
    conversor("Colombianos", 3956)   

else:
    print("Ingresa una opción válida por favor")