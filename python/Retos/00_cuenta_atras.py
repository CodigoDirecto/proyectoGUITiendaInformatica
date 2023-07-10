### Cuenta atrás ####

"""
Reto #27: CUENTA ATRÁS
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
"""
from threading import Thread
from time import sleep


def count_dow(start: int, seconds: int):

        if type(start) == int and start > 0 and type(seconds) == int and seconds > 0:
                for number in range(start, -1, -1):
                        print(number)
                        # sleep () hace pausas
                        sleep(seconds)
        else:
                raise Exception("Los parámetros deben ser enteros.")
        
# crear un hilo paralelo        
thread = Thread( target=count_dow, args = (10,1)).start()


count_dow(10,2)

print("Boom¡¡¡ ")