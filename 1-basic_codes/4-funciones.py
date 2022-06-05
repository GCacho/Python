# FUNCIONES
# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('¡Estoy aprendiendo a usar funciones!: ')

# imprimir_mensaje() #invoca la función

#-----------------------------------------------------------


# FUNCIONES CON PARÁMETROS
def conversacion(mensaje):
    print('Hola')
    print('Cómo estás')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opción (1,2,3): '))
if opcion == 1:
    conversacion('Elegiste la opción 1') #Pinta el mensaje anterior junto con el parametro ingresado
elif opcion == 2:
    conversacion('Elegiste la opción 2')

elif opcion == 3:
    conversacion('Elegiste la opción 3')
else:
    print('Escribe la opción correcta')

#-------------------------------------------------------

#Función para ingresar parámetros
# def suma(a,b):
#     print('Se suman dos números')
#     resultado = a + b                     #Se procesa el resultado
#     return resultado                      #Se regresa para poder guardarlo en una variable despues

# sumatoria = suma(1,4)                     #Guarda el return en una variable
# print(sumatoria)