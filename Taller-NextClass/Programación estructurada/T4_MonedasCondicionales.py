#Programa que calcula el valor de dolares a pesos

#Menu
menu = """
Bienvenido al conversor de monedas 🪙

1 - Pesos mexicanos
2 - Pesos argentinos
3 - Pesos colombianos 

Elige una opción: """
opcion = int(input(menu))

if opcion == 1:
    #Inicio bloque de código **Los bloques de código generalmente se almacenan en funciones**
    pesos = input("¿Cuántos pesos mexicanos tienes?")
    pesos = float(pesos) 
    valor_dolar = 20.05
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
    #Fin bloque de código
elif opcion == 2:
    #Inicio bloque de código
    pesos = input("¿Cuántos pesos argentinos tienes?")
    pesos = float(pesos) 
    valor_dolar = 103.86
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
    #Fin bloque de código
elif opcion == 3:
    #Inicio bloque de código
    pesos = input("¿Cuántos pesos colombianos tienes?")
    pesos = float(pesos) 
    valor_dolar = 4007
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
    #Fin bloque de código
else:
    print("Ingresa una opción válida por favor")

