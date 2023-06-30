### Exceptions Handling ###

# No hay programas libres de errores 
# Permiten que los programas no se paren por un error 

# Sintáxis
"""
try:
    código que puede fallar
except:
    si ocurre un error, se ejecutará este bloque
else:
    se ejecutará cuando no tenga ningún error
finally:
    se ejecuta independientemente de las otras opciones
"""

# Ejemplo con try y except

numberOne = 5
# numberTwo = 1
numberTwo = "1"
# Proboco el error ( exception ) sumo un número y una cadena de texto
# Try except
try:
    print( numberOne + numberTwo )
except:
# Y se ejecuta el esta linea al haber un error ( exception ) en la linea principal
# Si no hay errores no se ejecutará esta linea
    print("Python no puede sumar cadenas y números")


# Cambio el tipo de dato para que no de error
numberTwo= 1
# Try except else
try:
    print( numberOne + numberTwo )
except:
    print("Se ha producido un error")
else:
# Esta linea se ejecuta cuando no se ha producido error ( else )
    print("La ejecución continúa correctamente")
finally:
    # Se ejecuta finalmente sin importar los resultados del programa anterior
    print("La ejecución continúa")

# Exceptiones por tipo


# Try except else finally
try:
    print( numberOne + numberTwo )
except:
    print("Se ha producido un error")
else: # Opcional
# Esta linea se ejecuta cuando no se ha producido error ( else )
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta finalmente sin importar los resultados del programa anterior
    print("La ejecución continúa")



# Fuerzo el error otra vez cambiando el tipo de dato ( type error )
numberTwo = "1"
# Try except else finally ( tipo de error )
try:
    print( numberOne + numberTwo )

# Solo capturará errores de tipo de dato TypeError
except TypeError:
    print("Se ha producido un error de tipo de dato")
else: # Opcional
# Esta linea se ejecuta cuando no se ha producido error ( else )
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta finalmente sin importar los resultados del programa anterior
    print("La ejecución continúa")


# Fuerzo el error otra vez cambiando el tipo de dato ( value error )
numberTwo = "1"
# Try except else finally ( tipo de error )
try:
    print( numberOne + numberTwo )


# Solo capturará errores de tipo de dato ValueError y TypeError ( se pueden poner varias exceptions )
except ValueError:
    print("Se ha producido un error de tipo de dato")
except TypeError:
    print("Se ha producido un error")
else: # Opcional
# Esta linea se ejecuta cuando no se ha producido error ( else )
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta finalmente sin importar los resultados del programa anterior
    print("La ejecución continúa")


# También podemo guardar la información del error con 'as error'
try: 
    print(numberOne + numberTwo)
    print("No se ha producido el un error")
# nombre_para_el_error es el nombre de una variable ( arbitrario ) donde se guardará el error
except ValueError as nombre_para_el_error:
    print("error")
# Error es un error genérico ( captura todos los errores )
except Exception as mensajeError:
    print("error")

