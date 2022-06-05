# Operaciones de teoria de conjuntos con sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

#UNION
set_union = set1 | set2 # Con el pipe unimos los 2 sets y los unimos en 1 (Union)
print(set_union) # 1, 2, 3, 4, 5, 6, 7, 8

#INTERSECCION
set_interseccion = set1 & set2
print(set_interseccion)

#DIFERENCIA
set_diferencia = set1 - set2 #Se le restan los datos del set 2 al 1
print(set_diferencia)

#DIFERENCIA SIMETRICA
set_difsim = set1 ^ set2
print(set_difsim)
