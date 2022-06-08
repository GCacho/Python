set1 = {3, 5, 9, 3, 9}
set2 = set()
numbers = [1, 2, 3, 4, 5, 6, 1, 2]
set3 = set(numbers)

print(set1)
print(set2)
print(set3)
print(type(set1))

print('-------------')

set1.add(10)
print(set1)

print('-------------')
print('Interseccion')
print(set1.intersection(set3))

print(dir(set1)) #Muestra todos los metodos disponibles para set

#set1.difference(set3)
#set1.union(set3)
