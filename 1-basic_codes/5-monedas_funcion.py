#Programa que calcula el valor de dolares a pesos con funciones para acortar el código

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?")
    pesos = float(pesos) 
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


#Menu
menu = """
Bienvenido al conversor de monedas 🪙

1 - Pesos mexicanos
2 - Pesos argentinos
3 - Pesos colombianos 

Elige una opción: """
opcion = int(input(menu))

if opcion == 1:
    conversor("mexicanos", 20)
elif opcion == 2:
    conversor("argentinos" , 65)
elif opcion == 3:
    conversor("colombianos" , 3875)
else:
    print("Ingresa una opción válida por favor")

