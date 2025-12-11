# Ejercicio 3: Dada la siguiente tabla multidimensional, la cual almacena el salario mensual de los
# empleados (cada fila pertenece a un empleado distinto):
# int salarios[][] = { {700, 900, 1300, 800, 790, 850} , {1000, 950, 1080, 1070, 1200, 1100}, {1300,

# 930, 1200, 1170, 1000, 1000} , {1500, 1950, 1880, 1978, 2200, 2100} };

# implementa un método maxFila(int[][] tabla) que devuelve la posición de la fila cuya suma de
# todos sus datos es mayor.


def maxFila(tabla):

    max_suma = 0
    fila_max = 0

    for i in range(len(tabla)):
        suma_fila = sum(tabla[i])
        if suma_fila > max_suma:
            max_suma = suma_fila
            fila_max = i

    return fila_max


def main():
    salarios = [
        [700, 900, 1300, 800, 790, 850],
        [1000, 950, 1080, 1070, 1200, 1100],
        [1300, 930, 1200, 1170, 1000, 1000],
        [1500, 1950, 1880, 1978, 2200, 2100]
    ]

    fila_max = maxFila(salarios)
    print("La fila con la suma máxima es la fila:", fila_max)


if __name__ == "__main__":
    main()

