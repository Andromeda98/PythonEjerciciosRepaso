def segundo_mas_largo(strings):
    if len(strings) < 2:
        return "El array debe tener al menos 2 elementos"
    
    # Ordenar por longitud y eliminar duplicados de longitud
    strings_ordenados = sorted(set(strings), key=len, reverse=True)
    
    if len(strings_ordenados) < 2:
        return "No hay segundo elemento más largo (todos son iguales)"
    
    return strings_ordenados[1]

# Probar
array_strings = ["hola", "mundo", "python", "java", "c", "programación"]
resultado = segundo_mas_largo(array_strings)
print(f"Array: {array_strings}")
print(f"Segundo elemento más largo: '{resultado}'")