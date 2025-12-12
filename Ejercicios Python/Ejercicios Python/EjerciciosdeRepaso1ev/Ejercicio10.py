
# Ejercicio 10: Escribe un programa python que muestre por pantalla todos los
# posibles números de 3 dígitos que se pueden crear con los números 1, 2, 3 y
# 4. Además, debe devolver la cuenta del número total de posibilidades.
# 123
# 124
# ...
# 431
# 432
# Número total de números con 3 dígitos es 24

def mostrar_combinaciones():
    numeros = [1, 2, 3, 4]
    contador = 0

    for i in numeros:
        for j in numeros:
            for k in numeros:
                print(f"{i}{j}{k}")
                contador += 1

    print("Número total de números con 3 dígitos es", contador)


def main():
    mostrar_combinaciones()

main()
