def elementos_duplicados_strings(array):
    # Encontrar elementos que aparecen más de una vez
    elementos_vistos = set()
    duplicados = set()
    
    for elemento in array:
        if elemento in elementos_vistos:
            duplicados.add(elemento)
        else:
            elementos_vistos.add(elemento)
    
    return list(duplicados)

# Probar
array_strings = ["hola", "mundo", "python", "hola", "java", "python", "c"]
duplicados = elementos_duplicados_strings(array_strings)

print(f"Array: {array_strings}")
print(f"Elementos duplicados: {duplicados}")