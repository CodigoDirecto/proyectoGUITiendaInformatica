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
        self.full_name = f"{name} {surname}"
        # se hacen privados los atributos con __
        self.__name = name
        self.__surname = surname
    # Se pueden definir métodos|funciones ( acciones que puede hacer )
    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Colibrí" ,"Desarrollador")
# Una vez hechos privados los atributos ya no podemos accedes de otra forma que con getters y setters
# print(f"{my_person.name} {my_person.surname}")

# Llamada a la función del objeto ( nombre del objeto.nombre de la función)
my_person.walk()

# Podemos asignar valores a los atributos del objeto con el operador = y el operador . ( nombreObjeto.nombreAtributo = "nuevo valor" )
my_person.full_name = "Hétor de León ( el loco de los perros )"
# Este atributo al no ser privado se puede acceder sin get ni set
print(f"{my_person.full_name}")

