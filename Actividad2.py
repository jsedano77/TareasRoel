# 1.- Crea una tupla con una longitud de 5. usando diferentes tipos de datos.

# 2.- Cambiar la tupla a lista

#3.- Crea un diccionario donde la clave sea del 1 al 5 y los elementos los  datos de la lista

mitupla = ("Monterrey",True,2023,"Abril",10)
type(mitupla)
milista = list(mitupla)
type(milista)
milista
mikey = (1,2,3,4,5)
type(mikey)
mikeylist = list(mikey)
type(mikeylist)
midiccionario = {}
for key in mikeylist:
        for value in milista:
            midiccionario[key] = value
            milista.remove(value)
            break
print("Resultado midiccionario: " + str(midiccionario))
