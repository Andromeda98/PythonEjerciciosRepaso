
# Ejercicio 6: Implementa un programa Java con un método llamado
# insertElement(int[] tabla, int num, int index) que devuelve “tabla”,
# insertando el valor de “num” en el índice “index” pasado por parámetro.
# Como ya conocemos, las tablas tienen una longitud máxima que se indica
# al crearlas. Por lo tanto, para añadir este nuevo elemento deberemos
# desplazar el resto una posición hacia abajo. Es decir, si queremos



# def insertElement(tabla, num, index):
#     # Crear nueva tabla con tamaño + 1
#     nueva_tabla = [0] * (len(tabla) + 1)
    
#     # Paso 1: Copiar los elementos antes del índice
#     for i in range(index):
#         nueva_tabla[i] = tabla[i]
    
#     # Paso 2: Insertar el nuevo elemento
#     nueva_tabla[index] = num
    
#     # Paso 3: Copiar los elementos después del índice (desplazados)
#     for i in range(index, len(tabla)):
#         nueva_tabla[i + 1] = tabla[i]
    
#     return nueva_tabla

# # Ejemplo visual
# tabla_original = [10, 20, 30, 40, 50]
# print("Tabla original:", tabla_original)

# # Insertar 99 en la posición 2
# resultado = insertElement(tabla_original, 99, 2)
# print("Resultado:", resultado)