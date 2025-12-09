


def main():
    print("BIENVENIDO AL CORRECTOR DE EXAMENES")
    print("==========================================")

    respuestas_examen = []
    respuestas_alumno = []

    while True:
        print("\n¿Qué acción deseas realizar?")
        print("1. Introduce cuantas preguntas tiene el examen")
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
    
def IniciarExamen():
    longitud = int(input("¿Cuántas preguntas va a tener el examen: "))
    return longitud


def IngresarRespuesta(matriz, longitud):
    for i in range(longitud):
        respuesta = int(input(f"Ingresa la respuesta correcta del examen en la pregunta {i+1}: "))
        respuestas_examen.append(respuesta)


def IngresarRespuestaAlumno(matriz, longitud):
    for i in range(longitud):
        respuesta_alumno = int(input(f"Ingresa la respuesta correcta del examen en la pregunta {i+1}: "))
        respuestas_alumno.append(respuesta_alumno)