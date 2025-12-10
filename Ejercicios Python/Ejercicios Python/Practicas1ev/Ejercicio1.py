

def main():
    print("BIENVENIDO AL CORRECTOR DE EXAMENES")
    print("==========================================")



    respuestas_examen = []
    respuestas_alumno = []

    while True:
        print("\n¿Qué acción deseas realizar?")
        print("1. Introduce cuantas preguntas tiene el examen")
        print("2. Introduce las respuestas correctas del examen")
        print("3. Introduce las respuestas del alumno")
        print("4. Calificar examen")
        print("5. Salir")
        
        try:
            opcion = input("Ingrese el número de la acción deseada: ").strip()
            
            if opcion == '1':
                longitud = IniciarExamen()
            elif opcion == '2':
                IngresarRespuesta(respuestas_examen, longitud)
            elif opcion == '3':
                IngresarRespuestaAlumno(respuestas_alumno)
            elif opcion == '4':
                CalificarExamen(respuestas_examen, respuestas_alumno)
                print("¡Examen calificado!")
                print("Desea continuar corrigiendo otro examen? responda Y/N")
                if input().strip().upper() == 'Y':
                    respuestas_alumno.clear()
                    
            elif opcion == '5':
                print("¡Has elegido salir!")
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
    
def IniciarExamen():
    longitud = int(input("¿Cuántas preguntas va a tener el examen: "))
    return longitud


def IngresarRespuesta(matriz):
    for i in range(len(matriz)):
        respuesta = int(input(f"Ingresa la respuesta correcta del examen en la pregunta {i+1}: "))
        while respuesta < 0 :
            print("Respuesta no válida, debe ser un numero entero positivo. Inténtalo de nuevo.")
            respuesta = int(input(f"Ingresa la respuesta correcta del examen en la pregunta {i+1}: "))  
        matriz.append(respuesta)


def IngresarRespuestaAlumno(matriz):
    for i in range(len(matriz)):
        
        respuesta_alumno = int(input(f"Ingresa la respuesta del alumno en la pregunta {i+1}: "))
        while respuesta_alumno < 0 :
            print("Respuesta no válida, debe ser un numero entero positivo. Inténtalo de nuevo.")
            respuesta_alumno = int(input(f"Ingresa la respuesta del alumno en la pregunta {i+1}: "))
        matriz.append(respuesta_alumno)

def CalificarExamen(respuestas_examen, respuestas_alumno):

    numAcertadas = 0


    for i in range(len(respuestas_examen)):
        if respuestas_examen[i] == respuestas_alumno[i]:
            numAcertadas += 1
    print(f"\nEl alumno ha acertado {numAcertadas} preguntas de {len(respuestas_examen)}.")



if __name__ == "__main__":
    main()