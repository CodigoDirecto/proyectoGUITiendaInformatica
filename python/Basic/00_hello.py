# Variables
# Nomenclatura "Snake Case" y no "notacion camello" 
my_variable = "My String variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

# transformar en una cadena de texto con str()
my_int_to_str_variable = str(my_int_variable)

print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# argumentos separados por comas ( crea una cadena ) se puede pasar cualquier tipo de dato
print(my_variable,str(my_int_variable),my_bool_variable)
print("Este es el valor de : ",my_bool_variable)


# Funciones  del sistema len() la longitud
print(len(my_int_to_str_variable))
print(len(my_variable))

# Variables en una sola línea ( no abusar de esta forma de declarar variables )
name, surname, alias, age = "Colibrí","Desarrollador", "ColibriDesarrollador", 41

print("Me llamo",name,surname,".Mi edad es:",age, ". Y mi alias:", alias)

"""
name = input(" ¿ Cuál es tu nombre ? ")
age = input(" ¿ Cuál es tu edad ? ")

print("Nombre:",name)
print("Edad:",age)
"""

# Cambio de tipos ( no es de tipado fuerte )
name = 35
age = "Juan"

print("Nombre:",name)
print("Edad:",age)


# ¿ Forzamos el tipado ? // tiene sentido en los input
address : str = "Mi dirección" 
address = 32
# El tipo cambia aunque se fuerce el tipo
print(type(address))

