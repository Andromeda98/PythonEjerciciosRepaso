# Ejercicio 2: viendo el auge de las máquinas de golosinas, el colegio ha decidido invertir en la
# empresa Sabor Dulce el total del presupuesto anual. Los futuros programadores de 1oH-V se
# han dado cuenta que el algoritmo que maneja las máquinas está anticuado, y no siempre
# funciona bien. Por ello, tras unas largas reuniones se ha decidido implementar un nuevo
# software en Java que gestione la compra de productos en las máquinas. El nuevo algoritmo
# mostrará el siguiente mensaje hasta que el usuario escriba fin:

# Y se quedará a la espera de que el usuario introduzca uno de los 3 posibles comandos:
# ● insertar [dinero]: Si el usuario introduce el comando insertar, se añade al sueldo actual
# el valor del dinero introducido. La máquina SÓLO ACEPTA monedas de 1 y 2 euros. Una
# vez introducido el dinero, muestra por pantalla el saldo actual.
# ● retirar [idProducto]: Si el usuario introduce el comando retirar, la máquina entrega al
# usuario el producto cuya id coincide con la [idProducto] seleccionada por el usuario. Si el
# dinero introducido por el usuario NO ES SUFICIENTE, la máquina muestra por consola
# un mensaje de error, indicando cuánto dinero le falta al usuario. Si no ha habido ningún
# problema durante la compra, muestra por pantalla el nombre del producto comprado
# junto al dinero restante que le queda al usuario.
# ● fin: Si el usuario introduce el comando fin, la máquina muestra por consola el dinero
# restante que devolverá al usuario y finaliza el programa.
# La máquina contiene un total de 5 productos (inventados por el programador para realizar las
# pruebas del software diseñado). Estos productos se almacenan en una tabla multidimensional
# String de 5 columnas y 3 filas. En la primera de ellas, se almacena el identificador del producto.
# En la segunda el precio en euros (SOLAMENTE PUEDEN VALER 1 O 2 EUROS), y en la
# tercera fila el nombre completo del producto. Un ejemplo sería el siguiente:
# ID “manzana” “patatas” “galletas”
# Precio “2” “1” “2”
# Nombre “Manzana Golden Verde” “Fritos Matutano” “Galletas Principito”


def logica_maquina(tabla):

    print ("Bienvenido a la máquina de golosinas Sabor Dulce")
    print ("Introduzca un comando (insertar [dinero], retirar [idProducto], fin):")
    saldo = 0

    while True:

        comando = input("Comando >")
        partes = comando.split()
        accion = partes[0]

        if accion == "insertar":
            print("Ha seleccionado insertar")
            dinero = int(input("Introduzca la cantidad de dinero a insertar (1 o 2 euros): "))
            if dinero == 1 or dinero == 2:
                saldo += dinero
                print(f"Dinero insertado. Saldo actual: {saldo} euros")
            else:
                print("Error: Solo se aceptan monedas de 1 o 2 euros.")

        elif accion == "retirar":
            print("Ha seleccionado retirar")

            id = int(input("Introduzca el ID del producto a retirar (0-4): "))
            precio_producto = int(tabla[1][id])
            nombre_producto = tabla[2][id]
            print(f"Producto seleccionado: {nombre_producto}, Precio: {precio_producto} euros")
            if saldo >= precio_producto:
                saldo -= precio_producto
                print(f"Producto {nombre_producto} entregado. Dinero restante: {saldo} euros")
            else:
                falta = precio_producto - saldo
                print(f"Error: Dinero insuficiente. Le faltan {falta} euros.")

        
        elif accion == "fin":
            print(f"Fin del programa. Devolviendo {saldo} euros.")
            break






def main():


    tabla_productos = [["1", "2", "3", "4", "5"],
                       ["2", "1", "2", "1", "2"],
                    
                       ["Manzana Golden Verde", "Fritos Matutano", "Galletas Principito", "Chicles Trident", "Coca-Cola"]]


    logica_maquina(tabla_productos)    





