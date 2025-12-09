matriz = [[0,0,0,0,1,0,0],
         [0,0,0,0,1,1,0],
         [1,1,1,1,1,1,1],
         [0,0,0,0,1,1,0],
         [0,0,0,0,1,0,0]]

def rotar_matriz(matriz):
    rotada = []

    for i in range(len(matriz[0])):  # Columnas se convierten en filas
        rotada.append([])
        for j in range(len(matriz)):  # Filas se convierten en columnas
            rotada[i].append(matriz[len(matriz)-1-j][i])
    return rotada  # ¡RETURN FUERA DEL BUCLE!

resultado = rotar_matriz(matriz)

# Mostrar mejor
print("Matriz original:")
for fila in matriz:
    print(fila)

print("\nMatriz rotada 90°:")
for fila in resultado:
    print(fila)