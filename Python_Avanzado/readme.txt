0 - Configuraciones
    Se crea un entorno virtual con pip install mypy
    Se crea el achivo .gitignore y evitamos mandar el entorno virtual.

1 - Typing estático
    Convertimos el ingreso de datos a código estático para que marque error en caso de enviar mal algún tipo de dato
    Ejemplo> def is_palindrome(string: str) -> bool: #Solo aceptará string de entrada y regresará un valor booleano.
    En el entorno virtual (venv) ingresa: (mypy palindrome.py --check untyped-defs) para mostrarnos el error en el código como si fuera un lenguaje compilado.

2)  Funciones Anidadas.
    Pueden contener distintos scopes las variables.
    Existen los scopes globales y locales para cada función, dependiendo de su jerarquía recordará los valores de las variables.

3) Closures
    Debemos tener una nested funcion.
    La nested function debe referenciar un valor de un scope superior.
    La función que envuelve a la nested function debe retornarla también.

4)  Decoradores
    Son una Función que revibe como parámetro otra función, le añade cosas
    y retorna una función diferente.

5) Iteradores
    Son estructura de datos avanzados para guardar datos infinitos.
    El ciclo “for” dentro de Python, no existe. Es un while con StopIteration.

6) Generadores
    Son iteradores sencillos que ayudan a almacenar secuencias infinitas.
    Son lo mismo que los iteradores pero con una sintaxis más sencilla.

7) Sets
    Son una colección desordenada de elementos únicos e inmutables. (No se repiten y no se pueden modificar.)
    Funcionan bien para trabajar con teoria de conjuntos.
    set1.union(set2)
    set1.symmetric_difference(set2)
    set1.difference(set2)
    set1.intersection(set2)

8) Fechas
    Son fechas sirven pa todo