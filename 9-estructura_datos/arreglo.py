#Este archico lo podemos importar a otro documento para trabajar 
#A través de import from array Array
import random

class Arreglo:

    
    def __init__(self, capacity, fill_value=None):  #Capacidad y tamaño
        self.items = list()                         #Aquí guardamos los elementos
        for i in range(capacity):                   #Añadimos los elementos
            self.items.append(fill_value)

        
    def __len__(self):              #Para obtener la longitud del elemento
        return len(self.items)      


    def __str__(self):              #Nos regrese como string los elementos.
        return str(self.items)


    def __iter__(self):             #Para recorrer con iterador los elementos
        return iter(self.items)


    def __getitem__(self, index):   #Obtenemos un elemento en especifico
        return self.items[index]

    
    def __setitem__(self, index, new_item): #Para remplazar elementos.
        self.items[index] = new_item        #Necesitamos el indice para saber cual remplazar


    def __setrandom__(self):
        for i in range(len(self)):  #Le agregamos numeros al arreglo
            self[i] = random.randint(1,10)

    
    def __sumarray__(self):         #Suma todos los numeros del interior del array.
        suma = 0
        for i in range(len(self)):
            suma = suma + self[i]
        return suma
        