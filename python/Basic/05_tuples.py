### Tuples ###
# Conjunto de valores
# Aparentemente parecidos a la las listas
# Sus valores son constantes ( no pueden ser modificados una vez dados sus valores )

# Definición con la plabra reservada tuple() ó solamente con poner = ()
my_tuple = tuple()
my_other_tuple = ()

# Se asignan valores entre paréntesis
my_tuple = (35, 1.64, "Colibrí", "Desarrollador")
print(type(my_tuple))
print(my_tuple)

# Acceder a una posición
print(my_tuple[1])
print(my_tuple[-1])
# print(my_tuple[6]) ERROR se sale de la tupla


# Tiene funciones que comparte con las listas

# Count devuele las ocurrencias del valor pasado por parámetro
print(my_tuple.count("Colibrí"))
print(my_tuple.count("algo"))

# Index devuelve la posición que ocupa el valor que se le pasa
print(my_tuple.index("Desarrollador"))
print(my_tuple.index(35))

# my_tuple[1] = 1.90 ERROR, no se pueden cambiar sus valores
# print(my_tuple)


# Sí se pueden concatenar imprimiendo
print(my_tuple + my_other_tuple)

# Se puede crear una nueva tupla con la concatenación de las dos
my_sum_tuple =  my_tuple + my_other_tuple
print(my_sum_tuple)

# Acceder a los elementos entre [n:m]
print(my_sum_tuple[3:6])

# Se puede cambiar el tipo de tupla a lista ( para hacer variables sus valores )
my_tuple = list(my_tuple)
print(type(my_tuple))

# my_tuple [4] = "ColibriDesarrollador"
my_tuple.insert(1, "Azul")
print(my_tuple)
print(type(my_tuple))

# Se pueden borrar 
# la tupla
del my_tuple
# print(my_tuple) ERROR aquí la tupla está borrada con 'del'