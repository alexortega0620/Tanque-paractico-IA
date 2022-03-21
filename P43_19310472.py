#Funciones Lambda
'''
import math
def area(radio):
	resultado = math.pi * radio * radio
	print(resultado)

area(2)

'''
import math

area = lambda radio: (math.pi * radio * radio)

print(area(2))