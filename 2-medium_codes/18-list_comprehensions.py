def run():
    # squares = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    squares = [i**2 for i in range(1,101) if i % 3 != 0] #[element / for element in iterable / if condition] [para cada elemento / en el iterable yo voy a guardar ese elemento / solo si se cumple la condicion]
    print(squares)

if __name__ == "__main__":
    run()