"""
Este programa de prueba ilustra cómo trabajar con ficheros en Python
haciendo uso de los recursos del módulo os y os.path.

Autor original (Java): Álvaro Juan Ciriaco
Versión Python: Adaptación
"""
import os

def mostrar_menu():
    print("Selecciona una opción: ")
    print("  1) Crear File usando ruta")
    print("  2) Crear File usando ruta + nombre")
    print("  3) Renombrar File pasando ruta y nuevo nombre")
    print("  4) Borrar File usando ruta")
    print("  5) Salir")

def main():
    mostrar_menu()
    opcion = int(input())

    while opcion != 5:

        if opcion >= 1 and opcion <= 4:

            # ===== OPCIÓN 1: Crear archivo con ruta completa =====
            if opcion == 1:
                ruta = input(
                    'Introduce la ruta completa del archivo a crear.\n'
                    'Recuerda usar "/" en lugar de "\\".\nEjemplo: C:/Usuarios/Documentos/archivo.txt\n→ '
                ).replace("\\", "/")

                # Crear carpetas intermedias si no existen
                os.makedirs(os.path.dirname(ruta), exist_ok=True)

                # Crear archivo
                with open(ruta, "w") as archivo:
                    pass

                print("Archivo creado correctamente en:", ruta)

            # ===== OPCIÓN 2: Crear archivo usando ruta + nombre =====
            elif opcion == 2:
                ruta = input("Introduce la ruta de la carpeta donde crear el archivo: ").replace("\\", "/")
                nombre = input("Introduce el nombre del archivo: ")

                # Crear carpetas si no existen
                os.makedirs(ruta, exist_ok=True)

                ruta_nombre = os.path.join(ruta, nombre)

                # Crear archivo
                with open(ruta_nombre, "w") as archivo:
                    pass

                print("Archivo creado correctamente en:", ruta_nombre)

            # ===== OPCIÓN 3: Renombrar archivo =====
            elif opcion == 3:
                ruta = input("Introduce la ruta del archivo a renombrar: ").replace("\\", "/")

                if os.path.exists(ruta):
                    nuevo_nombre = input("Introduce el nuevo nombre del archivo: ")
                    directorio = os.path.dirname(ruta)
                    ruta_nueva = os.path.join(directorio, nuevo_nombre) if directorio else nuevo_nombre

                    os.rename(ruta, ruta_nueva)
                    print("Archivo renombrado correctamente a:", ruta_nueva)
                else:
                    print("La ruta no existe.")

            # ===== OPCIÓN 4: Borrar archivo =====
            elif opcion == 4:
                ruta = input("Introduce la ruta del archivo a borrar: ").replace("\\", "/")

                if os.path.exists(ruta):
                    os.remove(ruta)
                    print("Archivo eliminado correctamente.")
                else:
                    print("La ruta no existe.")

        else:
            print("Opción incorrecta. Introduce un número entre 1 y 5.")

        # 🔑 Volver a mostrar menú y pedir opción
        print()
        mostrar_menu()
        opcion = int(input())

    print("Programa finalizado.")

# Ejecutar programa
if __name__ == "__main__":
    main()


# import os


# def mostrar_informacion(f):
#     """
#     Pre: ---
#     Post: Si existe un fichero cuyo nombre es igual al asociado al objeto [f],
#           informa por pantalla de los atributos y principales características
#           del fichero. En caso contrario no produce ningún resultado.
#     """
#     if os.path.isfile(f):
#         print()
#         print(" ---------------------")
#         print("| INFORMACIÓN DE FILE |")
#         print(" ---------------------")
#         print("| Nombre del fichero:                             ", os.path.basename(f))
#         print("| Ruta relativa del directorio del fichero:       ", os.path.dirname(f))
#         print("| Nombre del fichero (ruta relativa):             ", f)
#         print("| Nombre del fichero (ruta absoluta):             ", os.path.abspath(f))
#         print("| Tamaño del fichero (en bytes):                  ", os.path.getsize(f))
#         print("| Puede ser leído:                                ", os.access(f, os.R_OK))
#         print("| Puede ser escrito:                              ", os.access(f, os.W_OK))


# def mostrar_menu():
#     """
#     Pre: ---
#     Post: Muestra por pantalla el menú de la aplicación.
#     """
#     print("Selecciona una opción: ")
#     print("  1) Crear File usando ruta")
#     print("  2) Crear File usando ruta + nombre")
#     print("Opción seleccionada (0 para finalizar): ", end="")


# def main():
#     """
#     Pre: ---
#     Post: Presenta información por pantalla del fichero indicado por el usuario.
#     """
#     mostrar_menu()
#     opcion = int(input())

#     while opcion != 0:
#         if opcion == 1 or opcion == 2:
#             if opcion == 1:
#                 ruta_final = input("Escriba la ruta para File: ")
#                 f = ruta_final
#             else:
#                 ruta = input("Escriba la ruta para File (sin nombre): ")
#                 nombre = input("Escriba el nombre para File: ")
#                 f = os.path.join(ruta, nombre)

#             # Muestra información relevante del fichero
#             mostrar_informacion(f)
#         else:
#             print("¡Opción incorrecta. Indique un número válido!")

#         # Separación estética
#         print()
#         print("==================================================")
#         print()

#         mostrar_menu()
#         opcion = int(input())


# if __name__ == "__main__":
#     main()
