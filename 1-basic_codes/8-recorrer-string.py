def run():
    # nombre = input('Escribe tu nombre: ')
    # for letra in nombre: #Puedes hacer recorridos en ciclos for con la cantidad de caracteres de una palabra o frase
    #     print(letra)

    frase = input('Escribe una frase: ')
    for caracter in frase:
        print(caracter.upper())

if __name__ == '__main__':
    run()