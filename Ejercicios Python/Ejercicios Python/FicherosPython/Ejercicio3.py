import os

def main():
    print("¡Bienvenido al programa de escritura sobre ficheros de texto!")
    print("Indique la ruta del fichero a escribir. Ejemplo: /Ficheros/fichero1.txt")

    ruta = input("Introduce la ruta de la carpeta donde crear el archivo: ").replace("\\", "/")
    nombre = input("Introduce el nombre del archivo: ")

    if not nombre.endswith(".txt"):
        nombre += ".txt"

    # Crear carpetas si no existen
    os.makedirs(ruta, exist_ok=True)

    ruta_nombre = os.path.join(ruta, nombre)

    # Crear archivo vacío
    archivo = open(ruta_nombre, "w", encoding="utf-8")
    archivo.close()
    print("Archivo creado correctamente en:", ruta_nombre)

    # Bucle para pedir datos
    dato = input('Introduzca lo que desea escribir (una palabra o número entero), escriba "fin" para finalizar: ').strip()

    while dato.lower() != "fin":
        archivo = open(ruta_nombre, "a", encoding="utf-8")

        if dato.isdigit():
            archivo.write("- Número entero introducido por el usuario: " + dato + "\n")
            print(f"El número entero {dato} se ha escrito correctamente en el fichero: {ruta_nombre}")
        elif dato.isalpha():
            archivo.write(f'- Cadena de caracteres introducida por el usuario: "{dato}"\n')
            print(f'La cadena de caracteres "{dato}" se ha escrito correctamente en el fichero: {ruta_nombre}')
        else:
            print("No válido (frase o mezcla)")

        archivo.close()
        dato = input('Introduzca lo que desea escribir (una palabra o número entero), escriba "fin" para finalizar: ').strip()

    print("¡El programa ha finalizado! ¡Hasta luego!")

if __name__ == "__main__":
    main()
