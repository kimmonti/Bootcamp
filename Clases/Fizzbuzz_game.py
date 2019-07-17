# EJ1. Crear un codigo que permita imprimir fizz si un numero es divisible por 3, 
# buzz si es divisible por 5 y fizzbuzz si es divisible por ambos.

def fizzbuzz_game(number): #Creo una función para el juego
    if (number % 3 == 0) and (number % 5 == 0): #Primero corroboro que sea divisible por ambos
        return ("Fizzbuzz")
    elif number % 3 == 0: #Si no, pruebo con 3
        return ("Fizz")
    elif number % 5 == 0: #Si no, pruebo con 5
        return ("Buzz")
    else:
        return ("No es divisible por 3 o 5.")

print(fizzbuzz_game(90))
print(fizzbuzz_game(27))
print(fizzbuzz_game(10))

#Podría jugarse con listas o con la biblioteca random