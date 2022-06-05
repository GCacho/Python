#Programa para elegir un vehiculo
print("------------------")
print("Elige un vehículo:")
print("------------------")
coche = int(input("Pulsa 1 - Camioneta\nPulsa 2 - Coche \nPulsa 3 - Camion\n--->"))
print("------------------")
if coche == 1:
    print("Elegiste una Camioneta")
elif coche == 2:
    print("Elegiste un Coche")
else:
    print("Elegiste un Camion")