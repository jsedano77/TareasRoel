dictHub={"Yan":1,"Day":7,"Yar":5,"Rox":9,"Mel":3}

for i,j in dictHub.items():
    print("{0} escogio el numero {1}".format(i,j))

numeros=dictHub.values()

numeros_lista = list(numeros)

minimo=min(numeros_lista)

maximo=max(numeros_lista)

print("El valor minimo es",minimo)
print("El valor maximo es",maximo)
