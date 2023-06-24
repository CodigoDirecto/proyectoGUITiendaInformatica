### Lists ###

# no son tipo base, son estructuras ( array, arreglo, colección )

# Declaración
my_list = list()
my_other_list  = []

# Imprimir la longitud de la lista ( la longitud empieza desde 1 )
print(len(my_list))

my_list = [35, 24, 52, 30, 17]

print(my_list)
print(len(my_list))

# Acepta diferentes tipos de datos
my_other_list = [35, 1.65, "Colibrí", "Desarrollador"]

print(my_other_list)
# El tipo de dato es list
print(type(my_other_list))

# Acceder a los valores de las listas ( 0 es la posición 1 )
# Los números en negativo acceden desde la última posición a la primera

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-3])
print(my_other_list[-4])

# ERROR idex out of range
#print(my_other_list[4])
#print(my_other_list[-5])
#print(my_other_list[5])


# count() devuelve el número de ocurrencias del valor buscado
print(my_other_list.count("Colibrí")) # 1 pues hay una ocurrencia
print(my_other_list.count("hola")) # 0 pues no hay ocurrencias

# Desempaquetado ( debe haber tantas variables como valores tiene la lista )
# Se puede asignar un nombre ( una variable )  a cada posición de la lista

age, height ,name, surname = my_other_list

print(surname)

# Se puede hacer también a mano ( es necesario asignar un valor a cada variable )

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0],my_other_list[3]


print(age)

# Sumar listas ( concatenación de listas )
print(my_list + my_other_list)
# print(my_list * my_other_list) ERROR con *, -, /

# Se pueden cambiar los tipos de datos. Aquí pasa de ser lista a ser string
# my_list = "Hola Python"

print(my_list)
print(type(my_list))

# Hace una copia de la lista
my_new_list = my_list.copy()

# Insertar un elemento en una lista
my_other_list.append("Colibrí desarrolladores")
# Insertar en la posición n ( mueve las posiciones )
my_other_list.insert(2,"Azúl")
# Elimina el un valor dando la posición ( elimina la primera ocurrencia solamente )
my_other_list.remove("Azúl")

print(my_other_list)

# Elimina el último elemento y nos devuelve el valor eliminado ( se puede recoger )
print(my_list.pop())
print(my_list)

# También se puede decir el elemento de la posisión a eliminar
my_pop_element = my_list.pop(2)
print(my_pop_element)

# Elimina el elemento ocurrente con el valor pasado
my_other_list.remove("Colibrí")
print(my_other_list)

# Elimina todos los elemntos de la lista
my_list.clear()
print(my_list)

print(my_new_list)

# Se puede invertir la ordenación de forma inversa
my_new_list.reverse()
print(my_new_list)

# Se ordena la lista por defecto de menor a mayor o alfabético 
my_new_list.sort()
print(my_new_list)

# Se puede "preguntar" que hay en dos posiciones con [n:m]
print(my_new_list[1:3])