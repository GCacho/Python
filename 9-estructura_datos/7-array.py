from arreglo import Arreglo #Importamos nuestro propio modulo.
menu = Arreglo(5)           #Le asignamos una longitud al modulo
len(menu)                   #Checamos la longitud del menu  
print(menu)                 #Imprimimos el menu

for i in range(len(menu)):  #Le agregamos numeros al arreglo
    menu[i] = i + 1 

print(menu)
print(menu[3])

print(menu.__len__())       #A través de los metodos obtenemos la longitud del elemento
print(menu.__str__())       #Muestra en formato de string el menu
print(menu.__iter__())      #Muestra su iteracion
print(menu.__getitem__(2))  #Muestra el item en el indice 2
menu.__setitem__(2,50)      #En el indice 2 remplazamos el numero por 50
print(menu)                 #Lo imprimimos

menu.__setrandom__()
print(menu)

print(menu.__sumarray__())
