# Ejercicio 6: Escribe un programa Java que indique si dos Strings son rotación
# entre ellos.

# 1º String: Hola
# 2º String: aloH
# ¡SON ROTACIÓN!


def son_rotacion(p1, p2):

    if len(p1) != len(p2):
        print("No pueden ser rotación porque tienen diferente longitud")
        return

    # Recorremos los índices de p1
    for i in range(len(p1)):
        # comparamos letra a letra: p1 al revés con p2 normal
        if p1[-1 - i] != p2[i]:
            print("NO son rotación")
            return  # terminamos, ya sabemos que no son rotación

    print("¡SON ROTACIÓN!")


def main():
    print("Resolvemos el problema de las rotacion de las palabras")

    palabra1 = input("introduce la primera palabra")
    palabra2 = input("introduce la segunda palabra")

    son_rotacion(palabra1, palabra2)
