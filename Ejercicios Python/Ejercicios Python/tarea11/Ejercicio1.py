import random
lista_aleatoria = [random.randint(1, 100) for _ in range(20)]
print(lista_aleatoria)
lista_aleatoria.sort()
print(lista_aleatoria)

print(f"El segundo elemento mas pequeño del array es : {lista_aleatoria[1]}")
print(f"El segundo elemento mas grande del array es : {lista_aleatoria[-2]}")
