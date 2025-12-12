
# Ejercicio 16: Escribe un programa python que encuentre todos los pares de
# elementos enteros de un array que suman el valor escrito por el usuario.


def pares_que_suman(tabla, numero):
    pares = []

    # Recorremos todos los pares posibles
    for i in range(len(tabla)):
        for j in range(i+1, len(tabla)):  # j empieza en i+1 para no repetir pares
            if tabla[i] + tabla[j] == numero:
                pares.append((tabla[i], tabla[j]))

    return pares


def main():
    array = [11, 22, 4, 5, 34, 12, 34, 23, 24, 21, 17, 25, 16, 18, 14, 9, 8, 3, 2, 10, 1, 7, 13, 17, 27]

    print(f"El array de números que tenemos es: {array}")
    numeroUsuario = int(input("Introduce un número entero para encontrar qué pares suman ese número: "))

    resultado = pares_que_suman(array, numeroUsuario)

    if resultado:
        print(f"Pares que suman {numeroUsuario}: {resultado}")
    else:
        print(f"No hay pares que sumen {numeroUsuario}")


main()
