tabla = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12], 
    [13, 14, 15, 16]
]

print(f"La tabla antes de modificar: {tabla}")

numero = 5

def modificar(matrix, num):
    # Crear una nueva matriz para no modificar la original
    nueva_matrix = []
    
    for fila in matrix:
        nueva_fila = []
        for elemento in fila:
            nueva_fila.append(elemento * num)
        nueva_matrix.append(nueva_fila)
    
    return nueva_matrix

tablamodificada = modificar(tabla, numero)

print(f"La tabla después de modificar: {tablamodificada}")