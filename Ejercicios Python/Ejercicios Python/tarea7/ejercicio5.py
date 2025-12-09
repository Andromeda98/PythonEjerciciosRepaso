Strings = ["python", "cadena", "objeto", "recursivo"]
Strings2 = []

def CopyArray(tabla, tabla2):
    # Limpiamos tabla2 por si tenía contenido previo
    tabla2.clear()
    
    # Copiamos cada elemento de tabla a tabla2
    for elemento in tabla:
        tabla2.append(elemento)
    
    return tabla2

# Probamos la función
resultado = CopyArray(Strings, Strings2)
print(f"La tabla 1 se ha copiado en la tabla 2: {Strings2}")

# def CopyArray(tabla):
#     tabla2 = []  # Creamos nueva lista vacía
#     for elemento in tabla:
#         tabla2.append(elemento)
#     return tabla2

# # Uso:
# Strings = ["python", "cadena", "objeto", "recursivo"]
# Strings2 = CopyArray(Strings)
# print(f"Original: {Strings}")
# print(f"Copia: {Strings2}")




# 📌 Métodos más comunes para copiar una lista:

# Usar list()

# original = [1, 2, 3, 4]
# copia = list(original)
# print(copia)  # [1, 2, 3, 4]


# Usar slicing ([:])

# original = [1, 2, 3, 4]
# copia = original[:]
# print(copia)  # [1, 2, 3, 4]


# Usar .copy() (Python 3.3+)

# original = [1, 2, 3, 4]
# copia = original.copy()
# print(copia)  # [1, 2, 3, 4]

# 📌 Diferencia entre shallow copy y deep copy

# Si tu lista contiene listas dentro de listas u objetos mutables, las copias anteriores son superficiales, es decir, las sublistas se siguen compartiendo:

# import copy

# original = [[1, 2], [3, 4]]
# copia_shallow = original.copy()
# copia_deep = copy.deepcopy(original)

# original[0][0] = 99

# print(copia_shallow)  # [[99, 2], [3, 4]]  <-- se modificó también
# print(copia_deep)     