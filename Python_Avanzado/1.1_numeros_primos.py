def is_primo(numero: int) -> bool: #Hacemos que string sea si o si un int y devuelva un booleano
    contador = 0

    for i in range(1, numero + 1): #Para absorver el número ingresado por el usuario y detener el bucle en ese número.
        if i == 1 or i == numero: #Para saltar la primer vuelta si es 1 o el mismo ingresado por el usuario número
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

def run():
    print(is_primo("Hola")) #En caso de poner un string y correr: mypy numeros_primos.py --check-untyped-defs, nos mostrará el error en consola.

if __name__ == '__main__':
    run()