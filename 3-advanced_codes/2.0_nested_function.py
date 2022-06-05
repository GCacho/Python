#Las nested_functions son funciones dentro de otras funciones.

def main():
    a = 1

    def nested():
        print(a)

    nested()

main() #Arroja el 1 que se "Hereda" a nested.