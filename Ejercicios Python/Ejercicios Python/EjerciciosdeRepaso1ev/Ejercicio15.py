# Ejercicio 15: Escribe un programa Java que encuentre los elementos
# duplicados de un array de enteros.

def elementos_duplicados_enteros(array):
    # Encontrar elementos que aparecen más de una vez
    duplicados = []
    no_duplicados = []

    for numero in array:
        if numero not in no_duplicados:
            no_duplicados.append(numero)
        else:
            duplicados.append(numero)

    return duplicados
# Probar
array_enteros = [1, 2, 3, 4, 2, 5, 3, 6, 7, 1]
duplicados = elementos_duplicados_enteros(array_enteros)

print(f"Array: {array_enteros}")
print(f"Elementos duplicados: {duplicados}")