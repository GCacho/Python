class FabricaTelefonos():
    def __init__(self , marca , color): #Crea el objeto
        self.marca = marca
        self.color = color
        print("El objeto {} ha sido creado".format(self.marca))
    
    def __str__(self): #Otorga un mensaje descriptivo al objeto
        return "El objeto es {}".format(self.marca)
    
    def __del__(self): #Destruye el objeto
        print("El objeto {} ha sido destruido".format(self.marca))

telefono = FabricaTelefonos("Nokia" , "Negro")
print(telefono.marca)
print(telefono) #Se muestra la descripcion del objeto gracias al __str__