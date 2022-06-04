# [1, 1, 2, 2, 4] -> [1, 2, 4]

def remove_duplicates(some_list):
    set1 = set(some_list)
    return set1

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))

if __name__ ==  '__main__':
    run()