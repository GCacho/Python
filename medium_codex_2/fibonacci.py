def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Escribe el numero a calcular"))

print(fibonacci(n))