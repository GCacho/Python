
class Monster:

    def __init__(self, nombre, salud, ataque_dado, ataque_recibido, defensa, debilidad):
        self.nombre=nombre
        self.salud=salud
        self.ataque_dado=ataque_dado
        self.ataque_recibido=ataque_recibido
        self.defensa=defensa
        self._debilidad=debilidad

    def recibir_golpe(self):
        return self.salud - self.ataque_recibido
    
class Goblin(Monster):
    
    def __init__(self, ataque_recibido):
        nombre = "Goblin"
        salud = 10
        ataque_dado = 3
        defensa = 1
        debilidad = "Espada"
        super().__init__(nombre, salud, ataque_dado, ataque_recibido, defensa, debilidad)


if __name__ == "__main__":
    monster1 = Goblin(3)
    print(monster1)