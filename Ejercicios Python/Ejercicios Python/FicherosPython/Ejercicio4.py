import os

def main():
    # Lista de palabras que queremos buscar
    palabras_buscadas = ["el", "java", "no", "piadoso"]

    # Leer archivo y limpiar signos de puntuación
    archivo = open("ficheros/ejercicio4/texto.txt", "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    texto = ""
    for linea in lineas:
        linea = linea.strip()
        # Eliminar signos de puntuación
        for signo in [",", ";", ".", ":", "!", "?", "«", "»"]:
            linea = linea.replace(signo, "")
        texto += linea + " "  # unir todas las líneas en un solo string

    # Convertimos todo a minúsculas
    texto = texto.lower()

    # Dividir el texto en palabras
    palabras_texto = texto.split()


    print("EL TEXTO ACTUAL QUEDA: ")

    for palabra in palabras_texto:
        print(palabra, end=" ")

    for palabra in palabras_texto:
        if palabras_buscadas[0] == palabra:
            ocurrencia1 += 1
        elif palabras_buscadas[1] == palabra:
            ocurrencia2 += 1
        elif palabras_buscadas[2] == palabra:
            ocurrencia3 += 1
        elif palabras_buscadas[3] == palabra:
            ocurrencia4 += 1

    for palabra in palabras_buscadas:

        print(f"{palabra} -> ocurrencias{ocurrencia1} ")




if __name__ == "__main__":
    main()