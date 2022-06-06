from stacks import Stack

food = Stack()

food.push('ehh')
food.push('ham')
food.push('spam')

print(food.pop())   # Saca spam

print(food.peek())  # Muestra el item que esta hasta arriba

food.clear()        # Limpia el stack
