# Ejercicio 5: Escribe un programa Java que cuente y muestre todos los
# caracteres duplicados de un String.




def contar_duplicados(cadena):
    cadena_analizar = cadena.lower()
    if len(cadena) == 0:
        return "La cadena está vacía."
    elif len(cadena) == 1:
        return "La cadena debe tener al menos 2 caracteres."
    else:
        
        duplicados = 0
        caracteres_duplicados = []
        caracteres_no_duplicados = []
        for i in cadena_analizar:
            if i not in caracteres_no_duplicados:
                caracteres_no_duplicados.append(i)
            else:
                caracteres_duplicados.append(i)

    print (f"el numero de caracteres duplicados es: {len(caracteres_duplicados)} y los caracteres duplicados son: {caracteres_duplicados}")

def main ():

    Palabra = input("introduce una palabra")

    contar_duplicados(Palabra)


if __name__ == "__main__":
    main()








    







