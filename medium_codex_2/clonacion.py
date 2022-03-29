a = [1,2,3]
print(id(a))
b = a
print(id(b)) #Son el mismo objeto - ocupan el mismo espacio de memoria
c = list(a) #Hace una copia de seguridad de la lista a
print(id(c)) #Ya son diferentes objetos
