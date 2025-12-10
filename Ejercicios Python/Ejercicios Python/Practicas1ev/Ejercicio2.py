def imprimir_menu():
    print("\nBienvenido a mi primera calculadora en Python")
    print("Seleccione una opción: debe de ser un número entre 1 y 5")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir") 
    print("5. Salir")

    try:
        opcion = input("Ingrese el número de la acción deseada: ")
        if opcion == '1':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"La suma es: {num1 + num2}")
        elif opcion == '2':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"La resta es: {num1 - num2}")
        elif opcion == '3':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"La multiplicación es: {num1 * num2}")
        elif opcion == '4':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            if num2 == 0:
                print("Error: No se puede dividir por cero.")
            else:
                print(f"La división es: {num1 / num2}")
        elif opcion == '5':
            print("¡Has elegido salir!")
            return False
        else:
            print("Opción no válida. Por favor, selecciona 1-5.")
    except ValueError:
        print("Error: Por favor ingresa un número válido.")
    return True


def main():
    while imprimir_menu():
        pass


if __name__ == "__main__":
    main()





    