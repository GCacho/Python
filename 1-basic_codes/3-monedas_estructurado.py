#Programa que calcula el valor de dolares a pesos

#Menu
menu = """
Bienvenido al conversor de monedas 馃獧

1 - Pesos mexicanos
2 - Pesos argentinos
3 - Pesos colombianos 

Elige una opci贸n: """
opcion = int(input(menu))

if opcion == 1:
    #Inicio bloque de c贸digo **Los bloques de c贸digo generalmente se almacenan en funciones**
    pesos = input("驴Cu谩ntos pesos mexicanos tienes?")
    pesos = float(pesos) 
    valor_dolar = 20.05
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares")
    #Fin bloque de c贸digo
elif opcion == 2:
    #Inicio bloque de c贸digo
    pesos = input("驴Cu谩ntos pesos argentinos tienes?")
    pesos = float(pesos) 
    valor_dolar = 103.86
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares")
    #Fin bloque de c贸digo
elif opcion == 3:
    #Inicio bloque de c贸digo
    pesos = input("驴Cu谩ntos pesos colombianos tienes?")
    pesos = float(pesos) 
    valor_dolar = 4007
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares")
    #Fin bloque de c贸digo
else:
    print("Ingresa una opci贸n v谩lida por favor")

