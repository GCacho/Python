import random

lista_numeros = list(range(100))
print(lista_numeros)

print('---------Lists-------------')
pares = [numero for numero in lista_numeros if numero % 2 == 0]
print(pares) 

print('----------Dictionaries-----------')
student_uid = [1, 2, 3]
students = ['Juan', 'Jose', 'Larsen']
students_with_uid = {uid: student for uid, student in zip(student_uid, students)}
print(students_with_uid)

print('----------SETS-----------')
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 3))
print(random_numbers)
non_repeated = {numbers for numbers in random_numbers}
print(non_repeated)