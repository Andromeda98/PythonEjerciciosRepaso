# Ejercicio 19: Escribe un programa python que, dado un array de Strings,
# determine si sus elementos se leen igual de principio a final y a la inversa.

# Array: “Hola”, “Adios”, “Adios”, “Hola”
# ¡Los elementos se leen igual!

def son_iguales(tabla):

    longitud = len(tabla) - 1
    es_palindromo = True

    for i in range(len(tabla) // 2):
        if tabla[i] != tabla[longitud]:
            es_palindromo = False
            break
        longitud -= 1

    if es_palindromo:
        print("La tabla es palíndromo")
    else:
        print("La tabla no es palíndromo")



def main():

    arrayigual = ["Hola", "Adios", "Adios", "Hola" ]
    arraydiferente = ["Pepe", "alberto", "Fernando", "laura"]

    son_iguales(arrayigual)
    son_iguales(arraydiferente)

main()