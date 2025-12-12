# Ejercicio 8: Escribe un programa Java que convierta un número entero en un
# número binario.


def main():
    numeroEntero = int(input("dame un numero entero"))
    numeroBinario = bin(numeroEntero)

    print("El numero binario del entero que has introducido es: " + numeroBinario)


main()