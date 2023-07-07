### Diccionaries ###
# Almacena datos de tipo clave valor


# Declaración
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# ASignación de valores
my_other_dict = {"Nombre":"Colibrí", "Apellido":"Desarrollador", "Edad":35, 1:"Python"}

my_dict = {"Nombre":"Colibrí",
            "Apellido":"Desarrollador", 
            "Edad":35, 
            "Languajes": {"Python","Java","JavaScript"}
            }

print(my_dict)

# Cada clave es una posición, cada clave tiene uno  o más valores 
print(len(my_other_dict)) 
print(my_dict)

# Acceder a los valores mediante las claves
print(my_dict["Nombre"])

# Dar nuevos valores a las claves
my_dict["Nombre"] = "Miguel"
print(my_dict["Nombre"])

# Añadir otra clave: valor
my_dict["Calle"] = "Calle Colibrí"
print(my_dict)

# Eliminar un elemento del diccionario ( referenciado por la clave )
del my_dict["Calle"]
print(my_dict)

# Comprobar si contiene los algún clave ( así no busca por valor )
print("Nombre" in my_dict)
print("Colibrí" in my_dict)

# Obtener parejas de claves valor
print(my_dict.items())
# Obtener las claves
print(my_dict.keys())
# Obtener los valores
print(my_dict.values())
# Crear un diccionario vacío a partir de las claves de otro diccionario escogidas ( crea solo las claves )
my_new_dict = my_other_dict.fromkeys(("Nombre",1))
print(my_new_dict)
# Crear un nuevo diccionario con todas las claves de otro diccionario
my_new_dict = dict.fromkeys(my_other_dict)
# Crear un diccionario a partir de unas claves más otras nuevas
my_new_dict = dict.fromkeys(("Nombre",1 , "País"))
print(my_new_dict)
# Dar las claves a partir de una lista
my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list)
