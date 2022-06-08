1-Colecciones:
    Tipos de Colecciones
        -Dinamicas
        -Inmutables
    Estructuras Lineales
        -Ordenadas por posición
        -Solo el primer elemento NO tiene predecesor
            *Fila en el supermercado 
            *Pila de platos
    Jerárquicas
        -Ordenadas como un árbol invertido 
        -Solo el primer elemento NO tiene predecesor
        -Padres e Hijos
            *Sistema de directorios
            *Índices de Libros
    Grafos
        -Cada dato puede tener varios predecesores y sucesores
        -Estos se llaman "vecinos"
            *Rutas de vuelos aereos (varios nodos unidos)
    Desordenadas
        -No tienen orden particular
        -No hay predecesores o sucesores
            *Bolsa de canicas
            *Premios de lotería
    Ordenadas 
        -Impone un orden con una regla
            *Directorios Telefónicos
            
2-Operaciones:
    -Tamaño
    -Pertenencia
    -Recorrido
    -String
    -Igualdad
    -Concatenación
    -Conversión de Tipo
    -Insertar
    -Remover
    -Reemplazar
    -Acceder

3-Listas:
    -Propósito general
    -Estructura más utilizada
    -Tamaño dinámico
    -De tipo secuencial
    -Ordenable

4-Tuplas:
    -Inmutables (No se pueden añadir o cambiar)
    -Útiles para datos constrantes
    -Más rápidas que las listas
    -Tipo secuencial

5-Conjuntos/Sets:
    -Almacenan objetos no-duplicables
    -De acceso rápido
    -Aceptan operaciones lógicas
    -Son desordenados

6-Dicccionarios
    -Pares de llave/valor
    -Arrays asociativos (hash maps)
    -Son desordenados

7-Arrays
    -Elemento: Valor almacenado en las posiciones del array
    -Indice: referencia a la posición del elemento
    ***No pueden****
    *Agregar posiciones*
    *Remover posiciones*
    *Modificar su tamaño*
    *Su capacidad se define al crearse*


8-Arreglos 2d (Grid)
    -Arreglos de 2 dimensiones

9-Nodos y Singly linked listas (Linked Structures)
    -Consiste de nodos conectados a otros
    -Los más comunes son sencillos o dobles
    -No se accede por índice, sino por recorrido
    -Conceptos Claves
        -Data: Valor almacenado en nodos.
        -Next: Referencia al siguiente nodo
        -Previus: Referencia al nodo anterior
        -Head: Referencia al primer nodo
        -Tail: Referencia al último nodo
    -Implementación:
        -Implementar otras estructuras
        -Optimización
        -Listas y Colas
    -Linked List:
        -Hacer/rehacer operaciones en un editor de texto
        -Historial de un navegador
        
10-Stacks (pilas)
    -Colección Lineale
    -Basados en arrays o linked lists
    -LIFO (last in - last out)
    -Añadir: push
    -Remover: pop 
    -Top 
    -Bottom
    -Aplicaciones:
        -Invertir el orden de una lista
        -Implementar "Undo"
        -Mantener historiales
        -Backtracking
    -Stack vs List:
        -Similares, no iguales
        -List: append, pop
        -Es afectada por sus otros métodos
    -Tienen sus propios métodos.

11-Queues (colas)
    -FIFO: First in First out
    -Rear: Último Elemento
    -Front: Primer Elemento
    -Priority queues:
        -Se basa en FIFO con los elementos de mayor/menor prioridad.
        -Clientes preferenciales, pase flash, etc 

12-Queues en stacks

13-Queues en nodos
    -Para hacer referencia a elementos

14-Ejercicio Musical
    -Proyecto que simule un reproductor de musica

15-Comprehensions
    -Son constructos que nos permiten generar secuencias
    a partir de otras secuencias.
        -List Comprehension:
            -[element for element in element_list if element_meets_condition]
        -Dictionary Comprehension:
            -{key: element for element in element_list if element_meets_condition}
        -Set Comprehension:
            -{element for element in element_list if element_meets_condition}