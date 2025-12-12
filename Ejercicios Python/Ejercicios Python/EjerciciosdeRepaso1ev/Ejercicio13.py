# Ejercicio 13: Escribe un programa Java que muestre los elementos comunes
# de dos arrays de Strings.




def elementos_comunes(tabla1, tabla2):
    duplicados = []

    for palabra in tabla1:
        if palabra in tabla2:
            duplicados.append(palabra)

    return duplicados

# Probar
array1 = ["hola", "mundo", "python", "java"]
array2 = ["java", "c", "python", "javascript"]
comunes = elementos_comunes(array1, array2)

print(f"Array 1: {array1}")
print(f"Array 2: {array2}")
print(f"Elementos comunes: {comunes}")