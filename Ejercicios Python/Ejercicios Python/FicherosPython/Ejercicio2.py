import os

def main():

    dnies = []
    apellido1 = []
    apellido2 = []
    nombres = []
    lineas_finales = []

    archivo = open("ficheros/ejercicio2/personas.txt", "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    for linea in lineas:
        linea = linea.strip()
        if linea:
            partes = linea.split()

            dnies.append(partes[0])
            apellido1.append(partes[1])
            apellido2.append(partes[2])
            nombres.append(" ".join(partes[3:]))

    for i in range(len(dnies)):
        nombre_completo = nombres[i] + " " + apellido1[i] + " " + apellido2[i]
        puntos = max(0, 51 - len(nombre_completo))
        linea_completa = nombre_completo + "." * puntos + dnies[i]
        lineas_finales.append(linea_completa)

    print("Resultado final:")
    for linea in lineas_finales:
        print(linea)

if __name__ == "__main__":
    main()
