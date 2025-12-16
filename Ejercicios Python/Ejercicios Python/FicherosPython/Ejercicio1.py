"""
Este programa de prueba ilustra cómo trabajar con ficheros en Python
haciendo uso de los recursos del módulo os y os.path.

Autor original (Java): Álvaro Juan Ciriaco
Versión Python: Adaptación
"""

import os


def mostrar_informacion(f):
    """
    Pre: ---
    Post: Si existe un fichero cuyo nombre es igual al asociado al objeto [f],
          informa por pantalla de los atributos y principales características
          del fichero. En caso contrario no produce ningún resultado.
    """
    if os.path.isfile(f):
        print()
        print(" ---------------------")
        print("| INFORMACIÓN DE FILE |")
        print(" ---------------------")
        print("| Nombre del fichero:                             ", os.path.basename(f))
        print("| Ruta relativa del directorio del fichero:       ", os.path.dirname(f))
        print("| Nombre del fichero (ruta relativa):             ", f)
        print("| Nombre del fichero (ruta absoluta):             ", os.path.abspath(f))
        print("| Tamaño del fichero (en bytes):                  ", os.path.getsize(f))
        print("| Puede ser leído:                                ", os.access(f, os.R_OK))
        print("| Puede ser escrito:                              ", os.access(f, os.W_OK))


def mostrar_menu():
    """
    Pre: ---
    Post: Muestra por pantalla el menú de la aplicación.
    """
    print("Selecciona una opción: ")
    print("  1) Crear File usando ruta")
    print("  2) Crear File usando ruta + nombre")
    print("Opción seleccionada (0 para finalizar): ", end="")


def main():
    """
    Pre: ---
    Post: Presenta información por pantalla del fichero indicado por el usuario.
    """
    mostrar_menu()
    opcion = int(input())

    while opcion != 0:
        if opcion == 1 or opcion == 2:
            if opcion == 1:
                ruta_final = input("Escriba la ruta para File: ")
                f = ruta_final
            else:
                ruta = input("Escriba la ruta para File (sin nombre): ")
                nombre = input("Escriba el nombre para File: ")
                f = os.path.join(ruta, nombre)

            # Muestra información relevante del fichero
            mostrar_informacion(f)
        else:
            print("¡Opción incorrecta. Indique un número válido!")

        # Separación estética
        print()
        print("==================================================")
        print()

        mostrar_menu()
        opcion = int(input())


if __name__ == "__main__":
    main()
