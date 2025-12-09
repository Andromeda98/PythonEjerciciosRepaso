numero = int(input("Escribe un numero entero positivo: "))
print("n    n^2    n^3    n^4")
print("-" * 25)  # Línea separadora

for i in range(1, numero + 1):
    print(f"{i}    {i**2}    {i**3}    {i**4}")