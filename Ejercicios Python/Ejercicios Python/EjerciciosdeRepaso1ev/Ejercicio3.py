def contains_strings():
    # Pedir dos strings al usuario
    string1 = input("Introduce el primer string: ")
    string2 = input("Introduce el segundo string: ")
    
    # Comparar lexicográficamente
    if string1 in string2:
        print("El primer string esta contenido en el segundo")
    else:
        print("No esta contenido")

# Ejecutar el programa
contains_strings()