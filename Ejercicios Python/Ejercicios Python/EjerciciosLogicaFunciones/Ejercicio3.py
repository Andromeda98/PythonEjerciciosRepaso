def Agregar(matriz1, matriz2):
    articulo = input("Ingresa el nombre del nuevo artículo: ")
    matriz1.append(articulo)
    numero = int(input(f"Ingresa la cantidad inicial de {articulo}: "))
    matriz2.append(numero)
    print(f"¡El artículo '{articulo}' se ha agregado al inventario con una cantidad de {numero}!")

def Mostrar(matriz1, matriz2):
    print("\nInventario:")
    for i in range(len(matriz1)):
        print(f"- {matriz1[i]}: {matriz2[i]} unidades")

def Buscar(matriz1, matriz2):
    articuloABuscar = input("Ingrese el nombre del artículo que desea buscar: ")
    
    if articuloABuscar not in matriz1:
        print(f"El artículo '{articuloABuscar}' no se encuentra en el inventario.")
    else:
        indice = matriz1.index(articuloABuscar)
        print(f"El artículo '{articuloABuscar}' tiene {matriz2[indice]} unidades en inventario.")

def Actualizar(matriz1, matriz2):
    articuloActualizar = input("Ingresa el nombre del artículo para actualizar la cantidad: ")
    if articuloActualizar not in matriz1:
        print(f"El artículo '{articuloActualizar}' no se encuentra en el inventario.")
    else:
        indice = matriz1.index(articuloActualizar)
        cantidadNueva = int(input(f"Ingresa la nueva cantidad para {articuloActualizar}: "))
        matriz2[indice] = cantidadNueva
        print(f"¡La cantidad de '{articuloActualizar}' ha sido actualizada a {cantidadNueva} unidades!")

def main():
    print("Bienvenido al gestor de Inventario Navideño")
    print("=======================================================")
    
    Articulos = []
    CantidadArticulos = []
    
    while True:
        print("\n¿Qué acción deseas realizar?")
        print("1. Agregar nuevo artículo al inventario")
        print("2. Mostrar inventario completo")
        print("3. Buscar artículo por nombre")
        print("4. Actualizar cantidad de existencias de un artículo")
        print("5. Salir")
        
        try:
            opcion = input("Ingrese el número de la acción deseada: ").strip()
            
            if opcion == '1':
                Agregar(Articulos, CantidadArticulos)
            elif opcion == '2':
                Mostrar(Articulos, CantidadArticulos)
            elif opcion == '3':
                Buscar(Articulos, CantidadArticulos)
            elif opcion == '4':
                Actualizar(Articulos, CantidadArticulos)
            elif opcion == '5':
                print("¡Gracias por usar el gestor de inventario navideño!")
                break
            else:
                print("Opción no válida. Por favor, selecciona 1-5.")
                
        except KeyboardInterrupt:
            print("\n¡Programa interrumpido!")
            break
        except ValueError:
            print("Error: Por favor ingresa un número válido para la cantidad.")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()