# Tarea 7: Ejercicios sencillos sobre Tablas

# Ejercicio 1: Implementa un programa Java con un método llamado
# sum(int [] tabla) que muestre por pantalla el resultado de sumar todos los
# elementos de la tabla pasada como parámetro.





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