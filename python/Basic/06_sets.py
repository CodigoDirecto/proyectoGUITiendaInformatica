### Sets ###

# NO es una estructura ordenada ( no se puede acceder con nombre[n] )
# La forma de guardar elementos es desordenada
# No se pueden almacenar valores repetidos
# En lo demás tiene funciones parecidas a las listas y las tuplas

# Definición con set() ó con  {} ( los diccionarios también usan {} para declaración )
my_set = set()
my_other_set = {}


print(type(my_set))
print(type(my_other_set)) # Inicialmente lo reconoce como diccionario

# Una vez dados los valores lo reconoce como 'set'
my_other_set = {"Colibrí", "Desarrollador", 35}
print(type(my_other_set))

# Tamaño del set
print(len(my_other_set))
# No es una estructura ordenada
my_other_set.add("ColibriDesarrollador")
print(my_other_set)

# NO admite repetidos ( aunque no da error, no lo almacena )
my_other_set.add("ColibriDesarrollador")
print(my_other_set)

# Comprobación de si un elemento existe en un 'set'
print("Colibrí" in my_other_set)
print("Colibri" in my_other_set)

# Eliminando elementos
my_other_set.remove("Desarrollador")
print(my_other_set)

# Vacía el 'set' 
my_other_set.clear()
print(len(my_other_set))

# Elimina la estructura con 'del' 
del my_other_set

# print(my_other_set) ERROR puesto que ha sido eliminado con 'del'


# Se puede cambiar a una lista ( incluso con el mismo nombre )
my_set = {"Colibrí", "Desarrollador", 35}
my_list = list(my_set)
print(my_list) # Aunque ya se puede acceder con [n] la ordenación no está definida por el desarrollador

my_other_set = {"Java", "Bash","Python"}

# No se pueden duplicar elemntos iguales 
my_new_set = my_set.union(my_other_set)
print(my_new_set)
my_new_set = my_set.union(my_other_set)
print(my_new_set)

# Para introducir más valores se deben meter entre {} llaves
print( my_set.union(my_other_set).union({"JavaScript","SQL"}))

# Devuelve las dirferencias entre los dos ( el que más valores tiene llama la función *)
print(my_new_set.difference(my_set))