# class FabricaTelefonos():
#     marca = "Samsung"

#     def ElaborarHuawei(self):
#         self.marca = "Huawei"

# telefono = FabricaTelefonos()
# telefono.ElaborarHuawei()
# print(telefono.marca)

class FabricaTelefonos():
    def __init__(self , marca , color): #Init ahorra codigo
        self.marca = marca
        self.color = color

telefono = FabricaTelefonos('Huawei' , "Azul")
print(telefono.marca)
print(telefono.color) 