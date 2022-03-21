class Usuarios:
	def __init__(self, nombre, apellidos):
		self.nombre = nombre 
		self.apellidos = apellidos

	def imprime_datos(self):
		print('Nombre:',self.nombre, '\nApellidos:', self.apellidos)

usuario1=Usuarios('FRANCISCO','GUZMAN')
usuario1.imprime_datos()

# Esta es la subclase
class UsuariosPremium(Usuarios):
	pass
usuario2=UsuariosPremium("ALEJANDRO","ORTEGA")
usuario2.imprime_datos()

