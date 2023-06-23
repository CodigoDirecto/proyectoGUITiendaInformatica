### Strings ###

# definición comilla doble " "
my_variable = "My String"

# es igual comilla simple que doble

# comilla simple ' '
my_other_variable = 'My String'

# lomgitud de la variable
print(len(my_variable))
print(len(my_other_variable))

print(my_variable + " " + my_other_variable)

#Carácteres especiales \t \n ...
my_new_line_string = "\tEste es un String con tabulación"
print(my_new_line_string)

# escapar un carácter especial con \ 
my_scape_string = "\\tEste es un string \n escapado"
print(my_scape_string)



# Formateo string %s    numérico %d
name, surname, age = "Colibrí", "Desarrollador", 20

# con Format y {}
print("Mi nombre es {} {} y mi edad {}".format(name,surname,age)) # este es menos restrictivo
# función  %() y %s 
print("Mi nombre es %s %s y mi edad %s" %(name,surname,age)) #este es el más seguro

# otra forma es usar las variables en el lugar donde corresponden concatenando
print("Mi nombre es " + name + " " + surname + " y mi edad " + str(age)) # no es óptimo

# Otro método para formatear strings con f"" es necesaria la f antes del string
print(f"Mi nombre es {name} {surname} y mi edad {age}")




# Desenpaquetado de carácteres ( cada carácter se guarda en una variable )
lenguaje = "python"
a, b, c, d, e, f = lenguaje
print(a)
print(e)

# División ( otra forma de seleccionar carácteres de una variable [n:m]) desde n hasta m
language_slice = lenguaje[1:3] # donde empieza y donde acaba
print(language_slice)

language_slice = lenguaje[1:] # seleccionar desde donde empieza
print(language_slice)


language_slice = lenguaje[0:6:2]# seleccionar partes
print(language_slice)

# Reverse ( darle la vuelta con [::-1])
reversed_language = lenguaje[::-1]
print(reversed_language)

# Funciones

print(lenguaje.capitalize()) #pone primera en mayuscula
print(lenguaje.upper()) # string en máyuscula completamente
print(lenguaje.count("t")) #cuenta cantidad ocurrencias de "t"
print(lenguaje.isnumeric()) # boleano 
print(lenguaje.lower()) # cambia en minusculas el string
print(lenguaje.lower().isupper()) # funcion de lower boolean



