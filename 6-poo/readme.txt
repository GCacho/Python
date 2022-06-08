Estructura basica:

Clases / Objetos / Metodos / Atributos/ Instancias

Objeto -> Es la abstraccion de la clase, (su unidad por asi decirlo)

Clase -> Es el "molde" del objeto (con esto podemos hacer los objetos que se necesiten, algo asi como una superfuncion)

Metodos -> Son las acciones del objeto, su programacion, su cerebro, todo lo que el objeto sera capaz de hacer.

Atributos -> Son como las variables se podrian ver como sustantivos del objeto

Instancia -> Es lo mismo que el objeto, si la clase es: class hotel(): la instancia es hotel() cuando se manda a llamar / se crea de la siguiente forma: __init__ 

Pilares POO:

Encapsulamiento / Abstaccion / Herencia / Polimorfismo

Abstraccion -> Cuando abstraemos los datos de un objeto para generar un "molde" 

Encapsulamiento -> public / protected / default / private : para definir el tipo de clase /esconde las clases y Hace un dato inviolable o inalterable. imagen de ejemplo en carpeta img

Herencia -> hereda propiedades de la clase padre / Nos ayuda a crear clases a partir de otras

Polimorfismo -> Es sobreescribir un método / cambia el comportamiento del metodo de la clase padre.

Modularidad -> Un ejemplo son legos: varias piezas que en conjunto construyen algo más grande

Otros:

Método constructor -> Es el equivalente a la funcion en POO - Dan un estado inicial al objeto - Tiene el mismo nombre de la clase - Son los parámetros mínimos que necesita el objeto para que pueda vivir

Diagrama y explicacion UML de Uber ---> https://platzi.com/clases/1474-oop/17126-el-diagrama-uml-de-uber/

Decomposición ----> El proceso de descomponer problemas en pequeñas partes para tener más control sobre las piezas 

@Decoradores:

    -Los decoradores permiten extender y modificar el funcionamiento de las funciones.
    -Los decoradores envuelven a otra función y permiten ejecutar código antes y después de que es llamada.

    def lower_case(func):
        def wrapper():
            #execute code before
            result = func()
            #execute code after
            return result
        return wrapper