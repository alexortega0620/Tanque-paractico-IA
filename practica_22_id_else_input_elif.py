
#practica 22 input, else if elif

print("FRANCISCO ALEJANDRO ORTEGA GUZMAN 19310472\n")

edad=int(input("ingrese su edad: "))

if edad <= 0:
    print("nadie puede tener esa edad")

elif edad>=1 and edad<=17:
    print("eres menor de edad")

elif edad>=18 and edad<=120:
    print("eres mayor de edad")

else:
    print("edad no valida")
