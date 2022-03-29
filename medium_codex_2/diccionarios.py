diccionario = {
    'David' : 35,
    'Erika' : 32,
    'Jaime' : 50
}
print(diccionario.get('Juan', 30)) #Si no existe juan te regresa el 30
print(diccionario.get('David', 30)) #devuelve la edad de David ya que si existe en el diccionario
del diccionario['Jaime'] #Borra a Jaime del diccionario
existe = 'David' in diccionario #Para saber si existe algun elemento en el diccionario
print(existe)