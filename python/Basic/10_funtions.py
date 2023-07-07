### Funtions ###
# Encapsulan lógicas para solucionar problemas muy concretos
# Modularización de código
# Desencadenan una tarea
# Sintáxis, palbra reservada 'def' nombre y () parámetros

def my_function ():
# Todo lo que tiene una tabulación es lo que pertenece a la función
    print("Esto es una función")

# Llamada a la función ( se ejecuta el bloque de código perteneciente a la función )
my_function ()
my_function ()
my_function ()
# Llamado tres veces, tres veces ejecuta el bloque de la función


# Función con parametros
def sum_two_values(first_number: int,second_number: int): # No sirve de nada poner tipos a los parámetros ( puede que sirvan a modo de referencia )
    print(first_number+second_number)

# Para llamar a una función con parámetros es necesario pasar tantos valores como parámetros tiene la función
sum_two_values(23,33)
sum_two_values(2322,233)
# La función en este caso no comprueba ni maneja el string para hacer cálculos 
# Por esto mismo si le pasamos string los concatenará
sum_two_values("4","2")

# También se le pueden pasar número reales sin nigún tipo de problema
sum_two_values(2.3,3.3)


# Las funciones también pueden devolver parámetros ( con la palabra reservada return )
def sum_two_values_return(first_value, second_value):
    my_result =  first_value + second_value
    return my_result

# Al llamar a la función necesitamos recoger el valor y hacer algo con ello ( si no es así, no hará nada con lo que devuelve )
# RECUERDA que será necesario que la función tenga un 'return'
my_result = sum_two_values_return(10,5)

print(my_result)

# Recuerda 'f' es para que se impriman la variables que hay entre llaves ( sin f imprime literal lo que se pone entre llaves )
def print_name( name, surname ):
    print(f"{name} {surname}")


print_name("Colibrí","Desarrollador")

# También se puede definir a qué parámetro le asignamos cada valor
print_name(surname = "Desarrollador",name = "Colibrí")

# Se puede dar un valor por defecto a un parámetro para hacerlo opcional alias ="Sin alias"
def print_name_whit_default(name,surname,alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

# Con los parámetros obligatorios
print_name_whit_default("Colibrí","Desarrollador")
# Con todos los parámetros
print_name_whit_default("Colibrí","Desarrollador","Colibridesarrollador")

# Con el asterisco al lado se abre a recibir infinidad de parámetros (*text)
# Función con parámetros arbitrarios
def print_texts(*text):
    print(type(text))
    for element in text:
            print(element.upper())

print_texts("Hola", "Ptyhon", "Colibrí")
