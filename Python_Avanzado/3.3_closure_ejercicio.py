def make_division_by(n: int) -> int: #Utilizamos typing estático para evitar errores.
    #Tiene que regresa una funcion que divida x entre n
    def div(num: int) -> int:
        return num / n
    return div

division_by_3 = make_division_by(3)
print(division_by_3(18)) #Tiene que retornar 6

division_by_5 = make_division_by(5)
print(division_by_5(100)) #Tiene que retornar 20

division_by_18 = make_division_by(18)
print(division_by_18(54)) #Tiene que retornar 3