
# Ejercicio 3: Implementa un programa Java con un método llamado
# contains(String[] tabla, String cadena) que devuelva TRUE, sí o solo sí,
# alguno de los elementos de la tabla pasada como parámetro es igual al
# valor de la variable “cadena”.


Strings = ["python", "cadena", "objeto", "recursivo"]
palabra = "cadena"

def contains(lista_strings, palabra):
    for elemento in lista_strings:
        if elemento == palabra:
            return True  # Encontrado - salimos inmediatamente
    return False  # Si llegamos aquí, no se encontró en toda la lista

# Probamos la función
resultado = contains(Strings, palabra)
print(resultado)  # True