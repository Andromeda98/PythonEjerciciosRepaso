# Ejercicio 12: Escribe un programa python que muestre los elementos comunes
# de dos arrays de enteros.
def elementos_comunes(tabla1, tabla2):
    duplicados = []

    for numero in tabla1:
        if numero in tabla2:
            duplicados.append(numero)

    return duplicados


array1 = [1, 2, 3, 4, 5, 6]
array2 = [4, 5, 6, 7, 8, 9]

resultado = elementos_comunes(array1, array2)

# Opción 1: convertir lista a string
print("Elementos duplicados: " + str(resultado))

# Opción 2: f-string
print(f"Elementos duplicados: {resultado}")




# def elementos_comunes_enteros(array1, array2):
#     # Convertir a conjuntos y encontrar intersección
#     set1 = set(array1)
#     set2 = set(array2)
#     comunes = set1.intersection(set2)
    
#     return list(comunes)

# # Probar

# comunes = elementos_comunes_enteros(array1, array2)

# print(f"Array 1: {array1}")
# print(f"Array 2: {array2}")
# print(f"Elementos comunes: {comunes}")