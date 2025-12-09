def comparar_enteros():
    # Pedir dos números al usuario y convertirlos a enteros
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    
    # Comparar numéricamente
    if num1 == num2:
        print(f"{num1} == {num2}")
    elif num1 < num2:
        print(f"{num1} != {num2}")
        print(f"{num1} < {num2}")
    else:
        print(f"{num1} != {num2}")
        print(f"{num1} > {num2}")

# Ejecutar el programa
comparar_enteros()