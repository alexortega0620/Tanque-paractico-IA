
#in significa esta en.

platillos=["tacos","tortas","refrescos","lonches"]


print("FRANCISCO ALEJANDRO ORTEGA GUZMAN 19310472\n")
print("\tPlatillos en el menu:\n\t-Tacos\n\t-Tortas\n\t-Refrescos\n\t-Lonches\n")
entrada= input("introduce un platillo:")


if entrada in platillos:
    print("tu plastillo si esta en la lista")
else:
    print("tu platillo no esta en la lista")

#print('tortilla' in platillos)
