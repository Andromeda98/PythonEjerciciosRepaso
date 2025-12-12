# Ejercicio 14: Escribe un programa Java que encuentre los elementos
# duplicados de un array de Strings.


def elementos_duplicados_strings(array):
    # Encontrar elementos que aparecen más de una vez
    duplicados = []
    no_duplicados = []

    for palabra in array:
        if palabra not in no_duplicados:
            no_duplicados.append(palabra)
        else:
            duplicados.append(palabra)

    return duplicados


# Probar
array_strings = ["hola", "mundo", "python", "hola", "java", "python", "c"]
duplicados = elementos_duplicados_strings(array_strings)

print(f"Array: {array_strings}")
print(f"Elementos duplicados: {duplicados}")