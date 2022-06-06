import tarfile
from linked_list import SinghlyLinkedList

words = SinghlyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

current = words.tail

while current:              #Recorre todos los nodos
    print(current.data) 
    current = current.next

print("----------------------------")

for word in words.iter():
    print(word)

print("----------------------------")

words.search('spam')

print("----------------------------")

words.search('juice') # No lo muestra porque no existe

words.clear() # Limpia la estructura de datos
