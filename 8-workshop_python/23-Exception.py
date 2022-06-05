def run():
    while True:
        try:
            edad = int(input("Ingresa tu edad"))
            print("Tu edad es= ", edad)
            break
        except:
            print("Ingresaste un valor erroneo pon un número")
    
if __name__ == '__main__':
    run()