print("SUMA DE MATRICES")
print("================")
print("Las dimensiones de las matrices (filas y columnas) tienen que ser iguales en ambas matrices")

# Validar filas
while True:
    try:
        rows = int(input("¿Cuántas filas tendrá la matriz?: "))
        columns= int(input("¿Cuántas columnas tendrá la matriz?: "))
        
        if rows <= 0 or columns <= 0:
            print("❌ Error: El número de filas y de columnas debe ser un numero entero positivo mayor a 0")
        
       

        else:
            break
    except ValueError:
        print("❌ Error: Debes ingresar un número entero válido")

print(f"\nDimensiones válidas: {rows} filas X {columns} columnas")

# Crear matrices vacías
matriz = []


print("\nRellenamos la matriz")
for row_position in range(rows):
    row = []
    print(f"--- Fila {row_position} ---")
    for col_position in range(columns):
        elemento = int(input(f"Introduce el elemento [{row_position}][{col_position}]: "))
        row.append(elemento)
    matriz.append(row)  # ✅ CORRECTO: Agregar la fila SOLO UNA VEZ


print("\n🔹 MATRIZ :")
for fila in matriz:
    print(fila)

print("PROMEDIO DE CADA FILA")
print("========================================")
for i, fila in matriz:
    print(f"el promedio de la fila {i} es:")
    print(sum(fila)/(len(fila)))
