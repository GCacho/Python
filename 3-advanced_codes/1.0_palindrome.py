def is_palindrome(string: str) -> bool: #Hacemos que string sea si o si un string y devuelva un booleano
    string = string.replace(" ","").lower()
    return string == string[::-1]

def run():
    print(is_palindrome(1000)) #En caso de poner un int y correr: mypy palindrome.py --check-untyped-defs, nos mostrará el error en consola.

if __name__ == '__main__':
    run()