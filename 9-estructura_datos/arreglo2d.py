from arreglo import Arreglo


class Arreglo2d():
    #Represents a two-dimensional array.
    def __init__(self, rows, columns, fill_value = None): # Arreglo2d(3, 3)
        self.data = Arreglo(rows)
        for row in range(rows):
            self.data[row] = Arreglo(columns, fill_value)

    def get_height(self):
        #Returns the number of rows.
        return len(self.data)

    def get_width(self):
        #Returns the number of columns.
        return len(self.data[0])

    def __getitem__(self, index):
        #Supports two-dimensional indexing with [row][column].
        return self.data[index]

    def __str__(self):
        #Returns a string representation of the grid.
        result = "" #Crea la variable

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "

            result += "\n"

        return str(result)