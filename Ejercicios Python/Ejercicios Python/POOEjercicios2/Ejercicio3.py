class Matriz:
    def __init__(self, rows, cols, matrix=None):
        self._rows = rows
        self._cols = cols
        
        if matrix is None:
            # Crear matriz vacía si no se proporciona
            self._matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            # Validar que la matriz proporcionada coincida con las dimensiones
            if len(matrix) != rows or any(len(fila) != cols for fila in matrix):
                raise ValueError("Las dimensiones de la matriz no coinciden con rows y cols")
            self._matrix = matrix

    # getNumberRows(): devuelve el número de filas de la matriz
    def getNumberRows(self):
        return self._rows

    # getNumberColumns(): devuelve el número de columnas de la matriz
    def getNumberColumns(self):
        return self._cols

    # setElement(int x, int j, int element): cambia el valor de la matriz en [x][j]
    def setElement(self, x, j, element):
        if 0 <= x < self._rows and 0 <= j < self._cols:
            self._matrix[x][j] = element
        else:
            raise IndexError(f"Índices [{x}][{j}] fuera de rango. Matriz: {self._rows}x{self._cols}")

    # addMatrix(int[][] matrix): suma matrices
    def addMatrix(self, matrix):
        # Verificar dimensiones
        if len(matrix) != self._rows or any(len(fila) != self._cols for fila in matrix):
            print("Error: No se puede sumar. Las matrices no tienen las mismas dimensiones.")
            return False
        
        # Sumar elemento por elemento
        for i in range(self._rows):
            for j in range(self._cols):
                self._matrix[i][j] += matrix[i][j]
        return True

    # multMatrix(int[][] matrix): multiplicación elemento por elemento (Hadamard)
    def multMatrix(self, matrix):
        # Verificar dimensiones
        if len(matrix) != self._rows or any(len(fila) != self._cols for fila in matrix):
            print("Error: No se puede multiplicar. Las matrices no tienen las mismas dimensiones.")
            return False
        
        # Multiplicar elemento por elemento
        for i in range(self._rows):
            for j in range(self._cols):
                self._matrix[i][j] *= matrix[i][j]
        return True

    # Método para obtener la matriz completa
    def getMatrix(self):
        return self._matrix

    # toString para mostrar la matriz
    def __str__(self):
        return "\n".join(" ".join(f"{elemento:4}" for elemento in fila) for fila in self._matrix)


# Programa de prueba
if __name__ == "__main__":
    print("=== PRUEBA DE LA CLASE MATRIZ ===\n")
    
    # Crear matriz 3x3
    matriz1 = Matriz(3, 3, [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    print("Matriz 1 inicial:")
    print(matriz1)
    print(f"\nFilas: {matriz1.getNumberRows()}")
    print(f"Columnas: {matriz1.getNumberColumns()}")
    
    print("\n" + "="*40)
    
    # Probar setElement
    print("Después de setElement(1, 1, 99):")
    matriz1.setElement(1, 1, 99)
    print(matriz1)
    
    print("\n" + "="*40)
    
    # Probar addMatrix
    matriz_suma = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
    
    print("Sumando matriz:")
    print(Matriz(3, 3, matriz_suma))
    print("\nResultado de la suma:")
    matriz1.addMatrix(matriz_suma)
    print(matriz1)
    
    print("\n" + "="*40)
    
    # Probar multMatrix
    matriz_multiplicacion = [
        [2, 1, 1],
        [1, 2, 1],
        [1, 1, 2]
    ]
    
    print("Multiplicando por matriz:")
    print(Matriz(3, 3, matriz_multiplicacion))
    print("\nResultado de la multiplicación (Hadamard):")
    matriz1.multMatrix(matriz_multiplicacion)
    print(matriz1)
    
    print("\n" + "="*40)
    
    # Probar errores
    print("Probando operaciones con dimensiones incorrectas:")
    matriz_erronea = [
        [1, 2],
        [3, 4]
    ]
    
    matriz1.addMatrix(matriz_erronea)  # Debería fallar
    matriz1.multMatrix(matriz_erronea)  # Debería fallar