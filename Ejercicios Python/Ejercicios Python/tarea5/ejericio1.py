print("Calcular si cuatro números son iguales")

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))
numero4 = int(input("Introduce el cuarto número: "))

if numero1 == numero2 and numero2 == numero3 and numero3 == numero4:
    print("Los cuatro números son iguales")
else: 
    print("Los cuatro números no son iguales")
