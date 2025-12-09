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