# Ejercicio 7: Escribe un programa Java que multiplique dos números binarios,
# escritos por el usuario.

def multiplicar_binarios(b1, b2):
    n1 = int(b1, 2)
    n2 = int(b2, 2)

    resultado = n1 * n2
    return bin(resultado)[2:]


def main():
    numero1 = input("Introduce un número binario: ")
    numero2 = input("Introduce el segundo número binario: ")

    print("El resultado en binario es:", multiplicar_binarios(numero1, numero2))


main()
