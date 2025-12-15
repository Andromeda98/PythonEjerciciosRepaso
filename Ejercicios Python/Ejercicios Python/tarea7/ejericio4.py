
# Ejercicio 4: Implementa un programa Java con un método llamado
# indexContains(String[] tabla, String cadena) que devuelva el índice de la
# tabla cuyo valor es igual al valor de “cadena”. En caso de no haber ningún
# valor igual, devuelve -1


Strings = ["python", "cadena", "objeto", "recursivo"]
palabra = "cadena"

def indexContains(tabla, cadena):
    for i in range(len(tabla)):
        if tabla[i] == cadena:
            return i  # Devuelve el índice si encuentra la palabra
    return -1  # Devuelve -1 si no la encuentra después de recorrer toda la lista

# Probamos la función
resultado = indexContains(Strings, palabra)
print(f"La palabra '{palabra}' se encuentra en la posición: {resultado}")

# Strings = ["python", "cadena", "objeto", "recursivo"]

# palabra = "cadena"
# print(f" La palabra {palabra} se encuentra en la posicion: {Strings.index(palabra)}")