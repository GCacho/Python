from fila_queue import ListQueue

food = ListQueue()
food.enqueue('eggs')
food.enqueue('ham')
food.enqueue('spam')

print(food.dequeue()) #Borra el primero

print("---------------")

food.traverse()

print("---------------")

food.enqueue('Huevos prro')

print("---------------")

food.traverse()
