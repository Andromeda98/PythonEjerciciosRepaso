def elementos_comunes_enteros(array1, array2):
    # Convertir a conjuntos y encontrar intersección
    set1 = set(array1)
    set2 = set(array2)
    comunes = set1.intersection(set2)
    
    return list(comunes)

# Probar
array1 = [1, 2, 3, 4, 5, 6]
array2 = [4, 5, 6, 7, 8, 9]
comunes = elementos_comunes_enteros(array1, array2)

print(f"Array 1: {array1}")
print(f"Array 2: {array2}")
print(f"Elementos comunes: {comunes}")