class Millas:
	def __init__(self):
		self._distancia = 0

	# Función para obtener el valor de _distancia
	# Usando el decorador property
	@property # ----------------------------> Getter es para datos de entrada
	def obtener_distancia(self): 
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia
	@obtener_distancia.setter # ----------------------------> Setter es para datos de salida
	def definir_distancia(self, valor):  
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		print("Llamada al método setter")
		self._distancia = valor

# Creamos un nuevo objeto 
avion = Millas()

# Indicamos la distancia
avion.distancia = 60

# Obtenemos su atributo distancia
print(avion.distancia) #? no toy seguro
