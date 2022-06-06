from nodos import Node

node1 = None
node2 = Node("A", None)
node3 = Node("B", node2)

print(node2)        #Imprime el nodo 2 en memoria

print(node2.data)   #Imprime los datos del nodo

print(node2.next)   #Imprime el siguiente dato del nodo

print(node3.next.data) #Imprime el nodo 2 porque ahi es donde apunta el next del nodo 3

node1 = Node("C", node3) #Cambiamos para que apunte al nodo 3

print(node1.next.data) #Deberia mostrar "B" (node3) porque ahi apunta el nodo 1 nuevo

head = None

for count in range(1, 5):
    head = Node(count, head)

while head != None:
    print(head.data)
    head = head.next

print("-------Operaciones en single linked structures---------")

head = None
for count in range(1, 6):
    head = Node(count, head)

while head != None:
    print(head.data)
    head = head.next

probe = head

while probe != None:
    print(probe.data)
    probe = probe.next

target_item = 2
while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    print(f"Target item {target_item} has been found!")
else:
    print(f"Target item {target_item} is not in the list")

probe = head
target_item = 3
new_item = "z"

while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    probe.data = new_item
    print(f'{new_item} replaced the old value in the node number {target_item}')
else:
    print(f"The target {target_item} is not in the linked list")

#insertar nuevo elemento

head = Node("F", head)
new_node = Node("k")
if head is None:
    head = new_node
else:
    probe = head
    while probe.next != None:
        probe = probe.next
    probe.next = new_node

#eliminar dato en nodo
removed_item = head.data
head = head.next
print(removed_item)

#Eliminar elemento del final
# if head.next in None:
#     head = None
# else:
#     probe = head 
#     while probe.next.next != None:
#         probe = probe.next
#     removed_item = probe.next.data
#     probe.next = None

# print(removed_item)
