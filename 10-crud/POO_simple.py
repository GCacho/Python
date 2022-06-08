class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')


if __name__ == '__main__':
    person1 = Person('Guillermo', 26)
    person2 = Person('Raul', 32)

    print(f'name1: {person1.name} === name2: {person2.name}')
    person1.say_hello()
    person2.say_hello()