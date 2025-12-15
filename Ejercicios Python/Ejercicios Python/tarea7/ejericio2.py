# Ejercicio 2: Implementa un programa Java con un método llamado
# average(double [] tabla) que devuelva un dato de tipo double, que
# indique la media de los valores de los elementos de la tabla pasada como
# parámetro.
# Ejercicio 3: Implementa un programa Java con un método llamado
# contains(String[] tabla, String cadena) que devuelva TRUE, sí o solo sí,
# alguno de los elementos de la tabla pasada como parámetro es igual al
# valor de la variable “cadena”.

# Ejercicio 4: Implementa un programa Java con un método llamado
# indexContains(String[] tabla, String cadena) que devuelva el índice de la
# tabla cuyo valor es igual al valor de “cadena”. En caso de no haber ningún
# valor igual, devuelve -1

# Ejercicio 5: Implementa un programa Java con un método llamado
# copyArray(String[] tabla, String[] tabla2) que devuelva “tabla2” con los
# mismos valores de “tabla”. Es decir, el programa debe copiar el contenido
# de una tabla en otra.

# Ejercicio 6: Implementa un programa Java con un método llamado
# insertElement(int[] tabla, int num, int index) que devuelve “tabla”,
# insertando el valor de “num” en el índice “index” pasado por parámetro.
# Como ya conocemos, las tablas tienen una longitud máxima que se indica
# al crearlas. Por lo tanto, para añadir este nuevo elemento deberemos
# desplazar el resto una posición hacia abajo. Es decir, si queremos

numeros = [2, 4, 6, 77, 8, 4]

suma = sum(numeros)
cantidad = len(numeros)
media = suma / cantidad

print(f"Suma: {suma}")
print(f"Cantidad de números: {cantidad}")
print(f"Media: {media}")


def calcular_media(lista_numeros):
    """
    Calcula la media (promedio) de una lista de números.
    
    Args:
        lista_numeros (list): Lista de números
        
    Returns:
        float: La media de los números
    """
    if len(lista_numeros) == 0:
        return 0  # Evita división por cero
    return sum(lista_numeros) / len(lista_numeros)

# Lista de números
numeros = [2, 4, 6, 77, 8, 4]

# Usar el método
resultado = calcular_media(numeros)
print(f"La media de {numeros} es: {resultado}")