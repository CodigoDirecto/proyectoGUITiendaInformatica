### Modules ###

# Similar al concepto de librería
# Se utiliza para estructurar y reutilizar código
# Importaciones
# Importante el nombre del fichero al crearlo para poder importarlo

# Palabra reservada 'import' y el nombre del fichero que queremos importar ( Python tiene librerías creadadas )
# Se puede importar la clase completa
import module

#También se puede importar una operación en concreto
from module import print_value

# Podemos importar un solo método de un archivo
# from  10_funtions import sum_two_values
# para poder importarlos no debe empezar por números el archivo
#nombre del fichero y nombre del método
# sum_two_values()

module.sum(3, 4, 5)
print_value("Hola Python")


# Un módulo de Python math
import math

print(math.pi)
print(math.pow(3,4))

# Un solo elemento de la clase
from math import pi 

print(pi)

# Se pueden renombrar los objetos importados
from math import pi as PI_NUMBER

print(PI_NUMBER)
