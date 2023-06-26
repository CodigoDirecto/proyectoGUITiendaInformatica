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