# Actividad 12
# Crea una función en la cual recibas como argumentos los  parámetros de una función cuadrática, y te regrese x1 y x2.

# ¡Importante hacerlo en Visual Studio!  Suerte

# Importar ‘sqrt’: Ya que para el resultado necesitamos calcular una raíz cuadrada, se importa la función

from math import sqrt

def saludo(primer_nombre,apellido):
   print("Hola," + primer_nombre + " " + apellido)

saludo("Roel","S")

# función con múltiples parámetros con una sentencia de retorno
def multiplica(val1, val2):
  return val1 * val2

va13 = multiplica(3, 5)  # muestra 15 en la consola
print(str(va13))



# 2 - Obtener los coeficientes de la ecuación: con la función ‘input()’ se le solicita al usuario  que 
# ingrese los valores de los coeficientes de la ecuación. Ya que la función ‘input()’  convierte la entrada en datos de tipo string, 
# se utiliza la función ‘int()’ para convertir los datos de tipo string a tipo int:

A = int(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = int(input("Ingrese el coeficiente de la variable lineal\n"))
C = int(input("Ingrese el término independiente\n"))

# 3 - segurar que la entrada de ‘sqrt()’ sea positiva: Ya que la raíz cuadrada de un numero negativo no existe, 
# es necesario que los valores que se le introduzcan a la función ‘sqrt()’ sean positivos. Es necesario manejar 
# también el caso en el que este valor sea negativo:

if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con numeros complejos")
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)  # Fórmula de Bhaskara parte positiva
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)  # Fórmula de Bhaskara parte negativa
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)

  