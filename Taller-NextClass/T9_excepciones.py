while True:
    try:
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es: ", edad)
    except:
        print("Ingresaste un valor erroneo.")