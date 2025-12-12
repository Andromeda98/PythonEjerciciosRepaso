# Ejercicio 17: Escribe un programa python que encuentre, en un array de
# enteros, los pares de elementos con mayor y menor separación entre ellos.

def main():
    # Array de ejemplo
    array = [11, 22, 4, 5, 34, 12, 34, 23, 24, 21, 17, 25, 16, 18, 14, 9, 8, 3, 2, 10, 1, 7, 13, 17, 27]

    # Ordenamos el array
    array.sort()
    print(f"Array ordenado: {array}")

    # Elementos con mayor distancia
    max_dist = (array[0], array[-1])
    print(f"Elementos con más distancia entre ellos: {max_dist[0]} y {max_dist[1]} (distancia = {max_dist[1]-max_dist[0]})")

    # Buscar elementos con menor distancia
    min_diff = array[1] - array[0]
    par_min = (array[0], array[1])

    for i in range(len(array)-1):
        diff = array[i+1] - array[i]
        if diff < min_diff:
            min_diff = diff
            par_min = (array[i], array[i+1])

    print(f"Elementos con menos distancia entre ellos: {par_min[0]} y {par_min[1]} (distancia = {min_diff})")

main()


# def main():
#     array = [11, 22, 4, 5, 34, 12, 34, 23, 24, 21, 17, 25, 16, 18, 14, 9, 8, 3, 2, 10, 1, 7, 13, 17, 27]
#     array.sort()
#     print(str(array))
#     longitud = int(len(array)/2)

#     print(f"Elementos con mas distancia entre ellos: {array[0]} y {array[-1]} ")
#     print(f"Elementos con menos distancia entre ellos: {array[longitud]} y {array[longitud+1]}")


# main()