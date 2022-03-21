# Esta es la superclase
class Usuarios:
	def __init__(self, nombre, apellidos):
		self.nombre = nombre 
		self.apellidos = apellidos

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)
usuario1=Usuarios("Alejandro","Ortega")
usuario1.imprime_datos()

# Esta es la subclase
class UsuariosPremium(Usuarios):
	def __init__(self, nombre, apellidos, instagram):
		Usuarios.__init__(self,nombre,apellidos)
		self.instagram = instagram
	def imprime_datos_premium(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos, '\nInstagram:', self.instagram)
usuario2=UsuariosPremium("Alejandro","Ortega","alexOrtega20")
usuario2.imprime_datos_premium()