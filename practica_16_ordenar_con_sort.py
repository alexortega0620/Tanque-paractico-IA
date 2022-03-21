
#ordenar lista con sort 

nombres=["alex","cielo","maria","francisco"]
nombres2=["alex","cielo","maria","francisco"]

print("FRANCISCO ALEJANDRO ORTEGA GUZMAN 19310472\n")


print("CASO 1\n")
print("nombres:\n\t0-alex\n\t1-cielo\n\t2-maria\n\t3-francisco\n")
print("las listas comienzan desde 0,1,2,3, en este caso los nombres se van a acomodar alfabeticamente, entonces nuestra lista quedaria:")
nombres.sort()
print(nombres)

nombres2.sort(reverse=True)


print("\nlas listas comienzan desde 0,1,2,3, en este caso los nombres se van a acomodar alfabeticamente al reves, entonces nuestra lista quedaria:")

print(nombres2)
