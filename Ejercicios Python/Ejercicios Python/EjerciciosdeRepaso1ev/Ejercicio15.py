def elementos_duplicados_enteros(array):
    elementos_vistos = set()
    duplicados = set()
    
    for elemento in array:
        if elemento in elementos_vistos:
            duplicados.add(elemento)
        else:
            elementos_vistos.add(elemento)
    
    return list(duplicados)

# Probar
array_enteros = [1, 2, 3, 4, 2, 5, 3, 6, 7, 1]
duplicados = elementos_duplicados_enteros(array_enteros)

print(f"Array: {array_enteros}")
print(f"Elementos duplicados: {duplicados}")