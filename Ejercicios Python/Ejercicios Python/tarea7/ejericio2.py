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