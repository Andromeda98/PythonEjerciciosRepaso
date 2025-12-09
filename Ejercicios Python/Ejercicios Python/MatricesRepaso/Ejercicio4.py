print("SUMA DE MATRICES")
print("================")
print("Las dimensiones de las matrices (filas y columnas) tienen que ser iguales en ambas matrices")

# Validar filas
while True:
    try:
        rows1 = int(input("¿Cuántas filas tendrá la matriz 1?: "))
        rows2 = int(input("¿Cuántas filas tendrá la matriz 2?: "))
        
        if rows1 <= 0 or rows2 <= 0:
            print("❌ Error: El número de filas debe ser mayor a 0")
        elif rows1 != rows2:
            print("❌ Error: Las filas deben tener la misma longitud")
        else:
            break
    except ValueError:
        print("❌ Error: Debes ingresar un número entero válido")

# Validar columnas
while True:
    try:
        columns1 = int(input("¿Cuántas columnas tendrá la matriz 1?: "))
        columns2 = int(input("¿Cuántas columnas tendrá la matriz 2?: "))
        
        if columns1 <= 0 or columns2 <= 0:
            print("❌ Error: El número de columnas debe ser mayor a 0")
        elif columns1 != columns2:
            print("❌ Error: Las columnas deben tener la misma longitud")
        else:
            break 
    except ValueError:
        print("❌ Error: Debes ingresar un número entero válido")

print(f"\nDimensiones válidas: {rows1} filas X {columns1} columnas")

# Crear matrices vacías
matriz1 = []
matriz2 = []

print("\nRellenamos la primera matriz")
for row_position in range(rows1):
    row = []
    print(f"--- Fila {row_position} ---")
    for col_position in range(columns1):
        elemento = int(input(f"Introduce el elemento [{row_position}][{col_position}]: "))
        row.append(elemento)
    matriz1.append(row)  # ✅ CORRECTO: Agregar la fila SOLO UNA VEZ

print("\nRellenamos la segunda matriz")
for row_position in range(rows2):
    row = []
    print(f"--- Fila {row_position} ---")
    for col_position in range(columns2):
        elemento = int(input(f"Introduce el elemento [{row_position}][{col_position}]: "))
        row.append(elemento)
    matriz2.append(row) 

print("\n🔹 MATRIZ 1:")
for fila in matriz1:
    print(fila)

print("\n🔹 MATRIZ 2:")
for fila in matriz2:
    print(fila)


matriz_suma = []

for row in range (len(matriz1)):
    new_row = []
    for column in range(len(matriz1[0])):
        new_row.append(matriz1[row][column]+matriz2[row][column])
    matriz_suma.append(new_row)

print("MATRIZ SUMA")
print("====================")
for fila in matriz_suma:
    print(fila)


# for row in matriz1:
#     for element in row:
#         print(element, end="")
#     print()


# for row in matriz2:
#     for element in row:
#         print(element, end="")
#     print()

# for row in matriz_suma:
#     for element in row:
#         print(element, end="")
#     print()