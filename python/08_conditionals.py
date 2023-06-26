### Conditionals ###
# Un condicional básicamente es que si se cumple una condición ( true ) se ejecuta el bloque de código dentro
# Sintáxis

# si es verdadero se ejecuta
# my_condition = True

# Si es falso no se ejecuta
my_condition = False

if my_condition: # la condición por defecto busca que sea True ( if my_condition == True: )
    print("Se ejecuta la condición del if")


my_condition = 5 * 3


# Todos los if son comprobadodos, en cambio los elif solo se comprueban si no se ha encontrado ninguna condición cumplida anteriormente

# si my_condition es igual a 10
if my_condition == 10:
    print("Se ejecuta la primera condición del primer if")

# su my_condition mayor que 10  y menor que 20
if my_condition > 10 and my_condition < 20:
    # Ejecutará todo lo que se encuentre tabulado a partir del condicional
    print("Es mayor que 10 y menor que 20")

#si no es la anterior comprueba esta condición con ( elif )
elif my_condition == 1: 
    print("Es igual a 1")

# y si no es ninguna quedará esta por defecto 
else:
    print("Es menor o igual que 10 mayor que  20")
    # Ejecutará todo lo que se encuentre tabulado a partir del condicional

# Esta linea ya se considera fuera de los condicionales puesto que no está tabulada
print("La ejecución continúa")


my_string = ""

if  my_string: # con el nombre de la variable a comprobar entre si tiene algún valor
    print("Mi cadena de texto no es vacía")

if my_string == "Mi cadena de textoooooooo": # Aquí comparamos la cadena con otra
    print("Estas cadenas de texto coinciden")

if not my_string: # con el not negamos la condición
    print("Mi cadena de texto es vacía")

