from queue_nodos import QueueNode

food = QueueNode()
food.enqueue('eggs')
food.enqueue('ham')
food.enqueue('spam')

print(food.head.data)

print(food.head.next.data)

print(food.tail.previous.data)