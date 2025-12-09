thislist = [100, 50, 65, 82, 23, 0, 0, -3, -44]

numCeros = 0
numPositivos = 0
numNegativos = 0

for i in thislist:
    if i == 0:
        numCeros += 1
    elif i < 0:
        numNegativos += 1
    else:
        numPositivos += 1

print(f"Lista: {thislist}")
print(f"→ Positivos: {numPositivos}")
print(f"→ Negativos: {numNegativos}")
print(f"→ Ceros: {numCeros}")