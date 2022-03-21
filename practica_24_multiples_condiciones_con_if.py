

#Multples condiciones utilizando el if


print("Bienvenidos invocadores\n\n"+ 
      "Estos son tus objetos disponibles para comprar:\n\n\t"+ 
      "Espadas:\n\t\t1-Espada nivel 1: 100monedas\n\t\t2-Espada nivel 2: 1200 monedas\n\t"+ 
      "Escudos:\n\t\t3-Escudo nivel 1: 100 monedas\n\t\t4-Escudo nivel 2: 750 monedas\n") 

comprar=[2,2,2]
dinero= 1500
espadan1= 100
espadan2= 1200

escudon1= 100
escudon2= 750

if 0 in comprar or comprar == []:
        print("especifique un numero entre 1 y 4")

if 1 in comprar:
    dinero= dinero - espadan1

if 2 in comprar:
    dienro= dinero - espadan2

if 3 in comprar:
    dinero=dinero - escudon1

if 4 in comprar:
    dinero= dinero - escudon2

if dinero<=0:
    print("ya no tienes dinero para comprar mas objetos")

if comprar == [1] or comprar == [2] or comprar == [3] or comprar == [4]:
    print("Te queda:" + str(dinero)+ " Monedas de oro\n","\tSe anadio el objeto a tu inventario")


    