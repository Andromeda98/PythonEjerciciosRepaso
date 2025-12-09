print("BIENVENIDO AL CONTADOR DE REGALOS NAVIDEÑO")
print("==========================================")


longitud = int(input("¿Cuántos niños recibieron regalos de santa quieres: "))

# Crear lista vacía
lista_nombres = []
lista_numRegalos = []

# Llenar la lista con bucle for
for i in range(longitud):

    nombre = input(f"Ingresa el nombre del niño {i+1}: ")
    lista_nombres.append(nombre)
    
    numero = int(input(f"Cuantos regalos recibio {lista_nombres[i]}: "))
    lista_numRegalos.append(numero)


promedio = sum(lista_numRegalos)/len(lista_numRegalos)

print("===========================================================================")
print(f"Santa Claus ha entregado un total de {sum(lista_numRegalos)} regalos de navidad")
print(f"En promedio cada niño recibio {promedio} regalos")
print(f"Felices Fiestas")