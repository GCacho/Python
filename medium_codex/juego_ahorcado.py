from random import randint


def run():
    palabra = []
    azar = randint
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            palabra.append(line)
        print(palabra)
    #letra=input("Ingresa una letra:\n--->")

if __name__ == "__main__":
    run() 