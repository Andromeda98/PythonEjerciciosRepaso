print("SUMA DE DIAGONALES")
print("================")
print("Las dimensiones de las matrices (filas y columnas) tienen que ser las mismas")

# Validar filas
while True:
    try:
        rows = int(input("¿Cuántas filas tendrá la matriz?: "))
        columns= int(input("¿Cuántas columnas tendrá la matriz?: "))
        
        if rows <= 0 or columns <= 0:
            print("Error: El número de filas y de columnas debe ser un numero entero positivo mayor a 0")
        
        elif rows!= columns:
            print("Error: El número de filas y de columnas deben de ser igual")

        else:
            break
    except ValueError:
        print("❌ Error: Debes ingresar un número entero válido")

print(f"\nDimensiones válidas: {rows} filas X {columns} columnas")

matriz = []

for row_position in range(rows):
    row = []
    print(f"--- Fila {row_position} ---")
    for col_position in range(columns):
        elemento = int(input(f"Introduce el elemento [{row_position}][{col_position}]: "))
        row.append(elemento)
    matriz.append(row)  # ✅ CORRECTO: Agregar la fila SOLO UNA VEZ

sumaDiagonalPrincipal = 0
sumDiagonaInversa = 0
n = len(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j == i:
            sumaDiagonalPrincipal+=matriz[i][j]


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j == (n-i-1):
            sumDiagonaInversa+=matriz[i][j]


print(f" La suma de la diagonal principal es: {sumaDiagonalPrincipal}")
print(f" La suma de la diagonal inversa es: {sumDiagonaInversa}")