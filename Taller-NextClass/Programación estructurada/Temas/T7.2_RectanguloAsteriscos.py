
def run():
    
    altura = int(input("Altura del rectangulo:\n----->"))
    ancho = int(input("Ancho del rectangulo:\n----->"))
    for i in range(altura):
        print('* ' * ancho)

if __name__ == '__main__':
    run()