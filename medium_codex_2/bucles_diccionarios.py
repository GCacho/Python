estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

for pais in estudiantes:
    print(estudiantes[pais])

for pais in estudiantes.keys():
    print(estudiantes[pais])

for numero_de_estudiantes in estudiantes.values():
    print(estudiantes[pais])

for pais, numero_de_estudiantes in estudiantes.items():
    print(estudiantes[pais])
    