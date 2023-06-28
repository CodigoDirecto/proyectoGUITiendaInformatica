### Classes ###

# La palabra reservada class y un nombre acorde con lo que vamos a hacer
# Los nombres de las clases para una buena práctica son ( camel case )
class MyEmpyPerson:
    # pass es para terminar ahí la definición si error ( por si no se mete más código )
    pass

# Llamada a la clase
# print(MyEmpyPerson())
# print(MyEmpyPerson)


class Person:
    # def __init__ es como se define el constructor ( self , param1, param2 )
    # self es el propio objeto ( se puede crear el objeto con valores literarles y parámetros vacíos )
    
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname
        self.full_name = f"{self.name} {self.surname}"
    # Se pueden definir métodos|funciones ( acciones que puede hacer )
    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Colibrí" ,"Desarrollador")
print(f"{my_person.name} {my_person.surname}")

# Llamada a la función del objeto ( nombre del objeto.nombre de la función)
my_person.walk()

# Podemos asignar valores a los atributos del objeto con el operador = y el operador . ( nombreObjeto.nombreAtributo = "nuevo valor" )
my_person.full_name = "Hétor de León ( el loco de los perros )"
print(f"{my_person.full_name}")
