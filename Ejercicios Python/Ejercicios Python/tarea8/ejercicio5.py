def ordenar_por_longitud(strings):
    # sorted() crea una nueva lista ordenada
    strings_ordenados = sorted(strings, key=len)
    return strings_ordenados

# Probemos
Strings = ["Laura", "Maria", "Alberto", "Andres"]
resultado = ordenar_por_longitud(Strings)
print("Ordenados por longitud (menor a mayor):", resultado)

print(f"El String de mayor longitud es: {resultado[-1]} y el String de menor longitud es: {resultado[0]}")