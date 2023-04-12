# Crear un programa que permita al usuario ingresar los montos de  las compras de un cliente 
# (se desconoce la cantidad de datos que se  cargarán, que pueden cambiar en cada ejecución), 
# cortando el  ingreso de datos cuando el usuario ingresa el monto 0.

# Si ingresa una cantidad negativa, no debe procesarse y se le debe  solicitar que ingrese una nueva cantidad. Al ﬁnalizar, informar el  total a pagar teniendo en cuenta que, si las ventas superan el total  de $ 1000, se debe aplicar un 10% de descuento.


# Basica 
total=0
contar=0
print("Introduzca los montos de compras (0 para salir):")
monto = int(input())
while monto != 0:
	if (monto>0):
	    total = total + monto
	    contar = contar + 1
	print("Intoduzca la n10ota de un estudiante (0 para salir): ")
	monto = int(input())
print ("promedio de notas del grado escolar es:" + str(total))
print ("Excelent")


# Avanzada
total=0
tarifa=25
print("Ingrese el tiempo en minutos del estacionamiento:")
tiempo = int(input())
while tiempo != 0:
    if (tiempo>0):	 
        if (tiempo <=60):
            total = total + 25
        else:
            if (tiempo/60>8):
                total = total + 200
            else:
                total = total + 25*(tiempo/60)
    print("Ingrese el tiempo en minutos del estacionamiento:")
    tiempo = int(input())
print ("promedio de notas del grado escolar es: " + str(total))
print ("Excelent")
