# Ejercicio 1: Implementa un programa Java que encuentre el segundo
# elemento más pequeño, y el segundo elemento mayor de un Array de
# enteros de longitud 20.

# Ejercicio 2: Implementa un programa Java que cree un Array de enteros
# de longitud 100 y lo rellene con enteros aleatorios entre 1 y 100 (ambos
# incluidos).

# Ejercicio 3: Implementa un programa Java que, dados dos Arrays de
# enteros, indique si ambos son exactamente iguales o no.

# Ejercicio 4: Implementa el mismo programa que el ejercicio anterior, pero
# para dos Arrays de Strings.



import random
lista_aleatoria = [random.randint(1, 100) for _ in range(20)]
print(lista_aleatoria)
lista_aleatoria.sort()
print(lista_aleatoria)

print(f"El segundo elemento mas pequeño del array es : {lista_aleatoria[1]}")
print(f"El segundo elemento mas grande del array es : {lista_aleatoria[-2]}")
