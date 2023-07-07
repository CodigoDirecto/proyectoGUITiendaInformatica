### Loops ###
# bucles, ciclos, iteradores

# while

# es necesario pasarle una condición
# es necesario que la condición cambie si entra en el bucle para que no se haga infinito
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
# se le pueden meter else a los while  opcionalmente
else:
    print("Mi condicióne es mayor o igual que 10")

print("La ejecución continua")

my_condition = 2
# if dentro de bucles
while my_condition < 20:
    my_condition+=1
    if my_condition == 15:
        print("Se detiene la ejecución")
        # break es para salir de la estructura 
        break
    print(my_condition)

print(my_condition)

# For
# Sirve para recorres un listado de elementos 
# Para hacer un determinado número concreto de vueltas
# Recorre uno a uno los elementos y lo guarda en la variable 'element' ( seleccionada arboitrariamente )
my_list = [35, 24, 52, 30, 17]

for element in my_list:
    print(element)

# "  "
my_tuple = (35, 1.64, "Colibrí", "Desarrollador")

for element in my_tuple:
    print(element)
# "  "
my_other_set = {"Colibrí", "Desarrollador", 35}
# " "
for element in my_other_set:
    print(element)


# Solo imprime las claves ( key )
my_other_dict = {"Nombre":"Colibrí", "Apellido":"Desarrollador", "Edad":35, 1:"Python"}

for element in my_other_dict:
    print(element)
# Podemos anidar condicionales para parar el bucle
    if element == "Edad":
        break
# Se le pueden insertar else como en el while
else: # El else no se ejecuta puesto que pertenece al bucle y nos salimos con el break de que la clave es "Edad"
    print(" El bucle for ha finalizado.")
# Muy atento a las tabulaciones puesto que son las que dicen a que pertence cada sentencia
# Una cosa es dentro de for y otra complementando al for
# Complementando al for solo se puede usar else

print("La ejecución continua")


for element in my_other_dict:
    print(element)
# Podemos anidar condicionales para parar el bucle
    if element == "Edad":
        continue # continue sirve para que obvie la vulta y comience con la siguiente
    print("Esto se ejecuta") # cunado la key sea "Edad" desde la parte continue no se ejecutará nada hasta la próxima vuelta
# Se le pueden insertar else como en el while
else: # El else no se ejecuta puesto que pertenece al bucle y nos salimos con el break de que la clave es "Edad"
    print(" El bucle for ha finalizado.")

