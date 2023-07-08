### List Comprehension ###
# Crear listas de forma rápida o a partir de otra

my_original_list = [1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

# Operación de sistema 'range'
my_range = range(8)
print(list(my_range))

# Crea una lista  a partir de otra lista ( primer i es el valor del la posición y la 2º i es donde irá el valor en la nueva lista )
my_list = [i for i in range(8)]
print(my_list)


def sum_five(number):
        return number+5
# Los valores pueden ser modificados antes introducidos en la nueva lista
my_list = [sum_five(i) for i in range(8)]
print(my_list)