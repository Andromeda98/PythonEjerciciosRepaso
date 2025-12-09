def elementos_comunes_strings(array1, array2):
    set1 = set(array1)
    set2 = set(array2)
    comunes = set1.intersection(set2)
    
    return list(comunes)

# Probar
array1 = ["hola", "mundo", "python", "java"]
array2 = ["java", "c", "python", "javascript"]
comunes = elementos_comunes_strings(array1, array2)

print(f"Array 1: {array1}")
print(f"Array 2: {array2}")
print(f"Elementos comunes: {comunes}")