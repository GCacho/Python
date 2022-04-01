
class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None # --1--
    

    @property
    def region(self):
        return self.__region


    @region.setter #Esta función restringe que puedan cambiar los datos los usuarios
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self.__pais}')


casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos']) # --2--
#print(casilla.region) #Regresa valor de None --1--
casilla.region = 'Ciudad de Mexico' #Regresa el valor pues arriba se especifico que si está esta región para acceder. --2--
#casilla.region = 'Cualquier_otra_ciudad' #Mandará error ya que la región no está especificada a la hora de crear el objeto. 
print(casilla.region)