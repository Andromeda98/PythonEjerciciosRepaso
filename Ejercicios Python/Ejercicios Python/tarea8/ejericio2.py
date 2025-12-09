thislist = [100, 50, 65, 82, 23, 0, 0, -3, -44]
numero = 5

print(thislist)

# Crear una nueva lista con los elementos multiplicados
resultado = []
for i in range(len(thislist)):
    if i != 0 and i != len(thislist) - 1:  # Excluir primero y último
        resultado.append(thislist[i] * numero)
    else:
        resultado.append(thislist[i])  # Mantener primero y último sin cambios

print(f"Lista original: {thislist}")
print(f"Lista modificada: {resultado}")
print(f"Lista sin el primero y el último (modificados): {resultado[1:-1]}")