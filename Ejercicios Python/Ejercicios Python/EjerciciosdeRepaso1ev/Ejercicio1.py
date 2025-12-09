def comparar_strings():
    # Pedir dos strings al usuario
    string1 = input("Introduce el primer string: ")
    string2 = input("Introduce el segundo string: ")
    
    # Comparar lexicográficamente
    if string1 == string2:
        print("Los strings son lexicográficamente iguales")
    else:
        print("Los strings NO son lexicográficamente iguales")

# Ejecutar el programa
comparar_strings()