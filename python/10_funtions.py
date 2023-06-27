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
def sum_two_values(first_number,second_number):
    print(first_number+second_number)

# Para llamar a una función con parámetros es necesario pasar tantos valores como parámetros tiene la función
sum_two_values(23,33)