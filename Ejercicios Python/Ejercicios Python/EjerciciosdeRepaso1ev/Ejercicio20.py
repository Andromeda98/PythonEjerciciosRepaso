
# Ejercicio 20: Crea una tabla multidimensional (2D) de números enteros y
# rellénala como te apetezca.
#  Escribe un método:
# public static int max(int[][] a)
# que devuelva el valor más grande del array.
#  Escribe un método:
# public static int rowSum(int[][] a, int x)
# que devuelva la suma de todos los elementos de la fila x
#  Escribe un método:
# public static int columnSum(int[][] a, int x)
# que devuelva la suma de todos los elementos de la columna x
#  Escribe un método:
# public static int[] allRowSums(int[][] a)
# que calcule la suma de todas las filas del array multidimensional, y
# almacene cada una de las sumas en un nuevo array simple, en el
# índice que corresponde. Es decir, el nuevo array contendrá en la
# posición 0, la suma de los elementos de la fila 0 del array
# multidimensional, y así sucesivamente.
#  Escribe un método
# public static boolean isRowMagic(int[][] a)
# que devuelva true, sí y solo sí, la suma de todas las filas del array
# multidimensional es la misma.
#  Escribe un método
# public static boolean isColumnMagic(int[][] a)
# que devuelva true, sí y solo sí, la suma de todas las columnas del
# array multidimensional es la misma.
def rellenar_matriz(filas, columnas):
    matriz = [][]

    for i in filas:
        for j in columnas:
            valor = int(input(f"introduce el valor de la matriz en la posicion {matriz [i][j]}"))
            matriz.append(valor)
        
    return matriz

def max(matriz):
    maximo = matriz[0][0]  # asumimos que el primer elemento es el mayor
    for fila in matriz:
        for valor in fila:
            if valor > maximo:
                maximo = valor
    return maximo


def main():

    print ("==============BIENVENIDO AL PROGRAMA DE LA TABLA MULTIDIMENSIONAL 2D==============")
    filas= int(input("introduce el numero de filas de la matriz "))
    columnas= int(input("introduce el numero de columnas de la matriz "))
    matriz = rellenar_matriz(filas, columnas)


    print("Elemento más grande de la matriz:", max(matriz))

main()