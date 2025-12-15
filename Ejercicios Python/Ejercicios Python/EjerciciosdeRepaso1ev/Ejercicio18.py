# Ejercicio 18: Dado un array de 10 elementos, debes separar sus elementos
# por la mitad y almacenarlos en dos arrays de 5 elementos cada uno de ellos.
# Array inicial:
# 58 24 13 15 63 9 8 81 1 78

# Arrays finales :
# 58 24 13 15 63
# 9 8 81 1 78



# def main():

#     arrayoriginal = [58,24,13,15,63,9,8,81,1,78]
#     array1 = []
#     array2 = []

#     mitad = int(len(arrayoriginal)/2)


#     for i in range(mitad):
#         array1.append(arrayoriginal[i])

#     for i in range(mitad +1, len(arrayoriginal)):
#         array2.append(arrayoriginal[i])

#     print(array1)

#     print(array2)

# main()

def main():

    arrayoriginal = [58,24,13,15,63,9,8,81,1,78]
    array1 = []
    array2 = []

    mitad = int(len(arrayoriginal) / 2)

    for i in range(mitad):
        array1.append(arrayoriginal[i])

    for i in range(mitad, len(arrayoriginal)):  # ← AQUÍ
        array2.append(arrayoriginal[i])

    print(array1)
    print(array2)

main()





