def run():

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break #Rompe el bucle completamente

    texto = input('Escribe un texto: ') #Recorre una letra por letra y corta el bucle cuando encuentra la letra 'o'
    for letra in texto:
        if letra == 'o':
            break
        print(letra)

if __name__ == '__main__':
    run() 