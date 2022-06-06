from arreglo2d import Arreglo2d

matrix = Arreglo2d(3, 3)

print(matrix)

for row in range(matrix.get_height()):
    for column in range(matrix.get_width()):
        matrix[row][column] = row * column

print(matrix.__str__()) #lo deja igual

print(matrix.get_height())
print(matrix.get_width())

print(matrix.__getitem__(2))
