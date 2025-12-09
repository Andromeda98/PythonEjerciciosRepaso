print("CREACIÓN DE MATRIZ IDENTIDAD")
print("============================")

# Pedir y validar el tamaño n
while True:
    try:
        n = int(input("Ingresa un número entero positivo n: "))
        if n > 0:
            break
        else:
            print("❌ Error: El número debe ser mayor a 0")
    except ValueError:
        print("❌ Error: Debes ingresar un número entero válido")

# Crear matriz identidad n x n
matriz_identidad = []

for i in range(n):
    fila = []
    for j in range(n):
        # Si estamos en la diagonal principal (i == j), poner 1, sino 0
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz_identidad.append(fila)

# Mostrar la matriz
print(f"\nMatriz identidad de tamaño {n}×{n}:")
for fila in matriz_identidad:
    print(matriz_identidad)