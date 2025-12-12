# Ejercicio 11: Escribe un programa Java que encuentre el segundo elemento
# más largo de un array de Strings.


def segundo_mas_largo(strings):
    if len(strings) < 2:
        return "El array debe tener al menos 2 elementos"

    # Inicializamos: ninguno encontrado aún
    mas_largo = ""
    segundo = ""

    for palabra in strings:
        # Si es más largo que el actual "mas_largo"
        if len(palabra) > len(mas_largo):
            # El más largo pasa a ser el segundo
            segundo = mas_largo
            # Y actualizamos el más largo
            mas_largo = palabra

        # Si no es el más largo, pero sí más largo que el "segundo"
        elif len(palabra) > len(segundo):
            segundo = palabra

    return segundo

# Probar
array_strings = ["hola", "mundo", "externocleidomastoideo", "java", "c", "programación"]
resultado = segundo_mas_largo(array_strings)
print(f"Array: {array_strings}")
print(f"Segundo elemento más largo: '{resultado}'")