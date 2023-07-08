### Challenges ###

"""

EL FAMOSO "FIZZ BUUZ":
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
Múltiplos de 3 por la palabra "fizz".
Múltiplos de 5 por la palabra "buzz".
Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

"""

my_var = 0

while (my_var <= 100):
    if my_var % 3 == 0 and my_var % 5 == 0 :
        print("fizzbuzz")
    elif my_var % 5 == 0:
        print("buzz")
    elif my_var % 3 == 0:
        print("fizz")
    else:
        print(my_var)
    my_var += 1



# Solución Mouredev

def fizz_buzz_moure ():
    # Función de sistea range(n,m) // donde n es el inicio y m es el final -1
    for index in range(1, 101):
        # Primero comprobar el caso mas restrictivo
        if index % 3 == 0 and index % 5 == 0:
            print("FizzBuzz")
        elif index % 5 == 0:
            print("Buzz")
        elif index % 3 == 0:
            print("Fizz")
        else:
            print(index)

fizz_buzz_moure()


"""
¿ES UN ANAGRAMA? ( dos string utilizan las mismas letras )
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word_one,word_two):
    if(word_one.lower() == word_two.lower()):
        return False
    # sorted() da una lista con las letras del string, lower() lo convierte a minusculas
    return sorted(word_one.lower()) == sorted(word_two.lower())
        

print(is_anagram("amor", "Roma"))