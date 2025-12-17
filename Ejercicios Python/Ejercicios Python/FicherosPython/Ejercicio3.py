import os

def main ():
    print("¡Bienvenido al programa de escritura sobre ficheros de texto!")
    print("Indique la ruta del fichero a escribir. Ejempo :/Ficheros/fichero1.txt")
    ruta = input("Introduce la ruta de la carpeta donde crear el archivo: ").replace("\\", "/")
    nombre = input("Introduce el nombre del archivo: ")

    # Crear carpetas si no existen
    os.makedirs(ruta, exist_ok=True)

    ruta_nombre = os.path.join(ruta, nombre)

    # Crear archivo
    with open(ruta_nombre, "w") as archivo:
        pass

    print("Archivo creado correctamente en:", ruta_nombre)



    dato = input('Introduzca lo que desea escribir, por ejemplo "Hola" o "3456", tiene que ser un numero o una palabra unica: ').strip()

    if dato.isdigit():
        print("Número entero")
    elif dato.isalpha():
        print("Palabra única")
    else:
        print("No válido (frase o mezcla)")


if __name__ == "__main__":
    main()

            

