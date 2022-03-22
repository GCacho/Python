#Programa que calcula el valor de dolares a pesos
pesos = input("¿Cuántos pesos tienes?")
pesos = float(pesos) 
valor_dolar = 20.05
dolares = pesos / valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")
