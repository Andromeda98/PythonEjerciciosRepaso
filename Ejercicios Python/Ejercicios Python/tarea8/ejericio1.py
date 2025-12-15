# Tarea 8: Ejercicios sobre Tablas

# Ejercicio 1: Implementa un método Java llamado calcularModa que
# calcule la moda de una tabla Java. La moda es el valor con mayor
# frecuencia que aparece en una colección de datos. Por ejemplo, si
# tenemos la tabla: {1, 1, 2, 1, 4, 1, 2, 1} la moda es 1.

# Ejercicio 2: Implementa un método Java llamado incrementarValores, el
# cual recibe una tabla y un valor numérico, y devuelve todos los elementos
# de la tabla multiplicados por dicho valor, excepto el primero y el último.
# Ejercicio 3: Implementa un método Java llamado estadisticasTabla, el
# cual recibe una tabla de enteros y muestra por pantalla: el número de
# enteros positivos, el número de enteros negativos, el número de 0s, el
# número de enteros pares y el número de enteros impares.

# Ejercicio 4: Implementa un método Java llamado copiarTabla, el cual
# recibe como parámetro una tabla de Strings, y devuelve una nueva tabla
# con los elementos en orden inverso.

# Ejercicio 5: Implementa un método Java llamado mayorYmenor, el cual
# recibe como parámetro una tabla de Strings y muestra por pantalla el
# String con mayor longitud y el String con menor longitud.



numeros = [2,4,6,77,8,4]

print(sum(numeros))


def calcular_suma(lista_numeros):
    """
    Calcula la suma de una lista de números.
    
    Args:
        lista_numeros (list): Lista de números
        
    Returns:
        int/float: La suma de los números
    """
    return sum(lista_numeros)

# Ejemplo de uso
numeros = [2, 4, 6, 77, 8, 4]
suma_total = calcular_suma(numeros)
print(f"La suma de {numeros} es: {suma_total}")

