my_set = {3, 4, 5}
print("My set = ", my_set) # 4, 3, 5 

my_set2 = {"Hola", 23.3, False, True}
print("My set 2 = ", my_set2) # Hola, False, True, 23.3 = Los muestra desordenados

my_set3 = {3, 3, 2}
print("My set 3 = ", my_set3) # 2, 3 porque 3 se repite

empty_set = {}
print(type(empty_set)) #Lo convierte en diccionario

empty_set = set()
print(type(empty_set)) #Asi se crea un set vacio

#Los sets sirven para eliminar los elementos repetidos
my_list = [1, 1, 2, 3, 4, 4, 5]
my_setlist = set(my_list)
print(my_setlist)

#Podemos añadir elementos a un set con .add
my_setlist.add("Nuevo Numero xd")
print(my_setlist)

# upgradear tambien
my_setlist.update((1, 7, 2),{62, 39})
print(my_setlist)

# Y Borrar datos
my_setlist.discard(3) #Tambien funciona con .remove, pero si no existe el dato mandara error
print(my_setlist)

#Borrar un dato aleatorio
my_setlist.pop()
print(my_setlist)

#Borrar todo el set
my_setlist.clear()
print(my_setlist)

my_set4 = {[1, 2, 3], 4}
print("My set 4 = ", my_set4) #Manda error porque la lista es mutable
