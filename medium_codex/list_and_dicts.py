def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "facundo", "lastname": "Garcia"}

    super_list = [
        {"firstname": "Facundo", "lastname": "Garcia"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Torres", "lastname": "Lopez"},
        {"firstname": "Susana", "lastname": "Cacho"},
        {"firstname": "José", "lastname": "Rodriguez"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],   
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.2, 2.6, 3.8, 4.2, 1.5],
    }

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == "__main__":
    run()