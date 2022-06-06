import queue
from queue_stacks import QueueStack

numbers = QueueStack()
numbers.enqueue(5)
numbers.enqueue(6)
numbers.enqueue(7)

print(numbers.inbound_stack)

numbers.dequeue()

print(numbers.inbound_stack) #Lo muestra vacio por el metodo

print(numbers.outbound_stack) #Muestra todos menos el 5 que se borro del primer stack



