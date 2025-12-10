# NOTAS: Junto al enunciado del examen se entregan los ficheros .java que el estudiante debe
# utilizar para resolver los ejercicios. Los ficheros NO SE PUEDEN MODIFICAR, únicamente se
# tiene que implementar y comentar el funcionamiento de los métodos indicados en el enunciado.
# En cada uno de los métodos main() entregados al estudiante se encuentran las pruebas que tiene
# que superar el código desarrollado para que el ejercicio esté correcto. Se entiende que la
# resolución de cada uno de los ejercicios no debe estar orientada únicamente a superar las pruebas
# proporcionadas. Un ejercicio que no supera más del 50% de las pruebas entregadas estará
# automáticamente suspendido.
# ENTREGA: Se debe entregar un fichero .zip con el siguiente formato
# PrimerApellido_Nombre.zip. Este fichero debe contener únicamente el paquete Java llamado
# PrimerApellido_Nombre_Examen, en el que se encuentran todos los ficheros .java
# proporcionados para el examen. Un fallo en la entrega resta 2 puntos en la puntuación total. Dos
# o más fallos es un suspenso automático del examen.
# ---------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 1: El cifrado del libro es un método de cifrado que utiliza un libro u otro texto como
# clave para codificar y decodificar mensajes. Es un tipo de cifrado por sustitución donde el remitente
# y el destinatario acuerdan un libro específico y comparten las instrucciones para encontrar las
# letras de la clave en el texto acordado.
# El procedimiento básico del cifrado de libro es el siguiente:
# • Selección del libro: Ambas partes acuerdan y poseen una copia idéntica del mismo libro,
# preferiblemente uno común y fácilmente disponible.
# • Definición de la clave: Se establece un método para identificar palabras en el libro. Por
# ejemplo, podrían usar el número de página y la palabra en esa línea como la ubicación de
# la palabra clave.
# • Cifrado del mensaje: El remitente busca cada palabra del mensaje en el libro y registra
# su ubicación de acuerdo con la clave predefinida (página, palabra).
# • Envío del mensaje cifrado: El remitente envía el mensaje codificado usando las
# ubicaciones del libro.
# • Decodificación del mensaje: El destinatario utiliza el mismo libro y clave para encontrar
# las ubicaciones de las palabras en el libro y descifrar el mensaje.
# Un ejemplo básico de su funcionamiento es el siguiente: Elegimos el libro "La vuelta al mundo en
# 80 días", queremos escribir de forma cifrada "JULES VERNE". Una posibilidad sería ésta:

# 39-30
# 53-2

# Y para decodificarlo:
# • Buscamos la página 39 y palabra 30, y vemos que corresponde a la palabra JULES
# • Buscamos la página 53 y segunda palabra, y encontramos la palabra VERNE

# Apellidos: Nombre: No.
# NOTA:

# Se pide diseñar un programa que dado un String, devuelva una nueva cadena de caracteres
# aplicando el cifrado del libro a aquellas palabras de cada línea que se encuentren detrás de un
# carácter ‘>’. Las palabras de las líneas en las que no aparece el carácter ‘>’ se copian sin aplicar
# ningún cifrado, al igual que las palabras que aparecen antes del carácter ‘>’ en las líneas que sí
# lo contienen. Es importante saber que, únicamente se cifran las palabras, nunca se cifrarán los
# espacios en blanco o cualquier otro carácter como puntos, comas, etc...
# Para facilitar la programación se va a utilizar un Array de cadena de caracteres de longitud 3,
# donde se almacena en cada una de las posiciones una página entera del libro ‘La Comunidad del
# Anillo’ de J.R.R Tolkien, siendo la primera página almacenada la asociada a la numeración 1. Hay
# que tener en cuenta que el texto adjunto es limitado, por lo tanto, no todas las palabras de nuestro
# lenguaje tendrán codificación usando el texto de prueba. NUNCA se deberá probar el texto con
# palabras con acentos o signos de puntuación. Para realizar cualquier prueba parcial del algoritmo
# a desarrollar, utiliza alguna de las pruebas unitarias adjuntadas.

# 4,25 puntos

# Ejercicio 2: se ha de diseñar e implementar el método multiplicar(int[] a, int b) y dividir(int[] a, int
# b) para mejorar la implementación de los números grandes llevada a cabo en la práctica 2 de la
# asignatura.
# La función multiplicar(int[] a, int b) debe permitir el cálculo de la multiplicación de un número
# grande con un tamaño de NUM_MAX_DIGITOS dígitos. El número entero [b] por el que se
# multiplica SIEMPRE va a ser de una única cifra. El resultado de la operación se almacena sobre
# la propia tabla [a], por lo tanto, se sobrescribe el resultado.
# La función dividir(int[] a, int b) debe permitir el cálculo de la división de un número grande con
# un tamaño de NUM_MAX_DIGITOS dígitos. El número entero [b] por el que se divide SIEMPRE
# va a ser de una única cifra. El resultado de la operación se almacena sobre la propia tabla [a], por
# lo tanto, se sobrescribe el resultado.

# 4,25 puntos

# Ejercicio 3: Dada la siguiente tabla multidimensional, la cual almacena el salario mensual de los
# empleados (cada fila pertenece a un empleado distinto):
# int salarios[][] = { {700, 900, 1300, 800, 790, 850} , {1000, 950, 1080, 1070, 1200, 1100}, {1300,

# 930, 1200, 1170, 1000, 1000} , {1500, 1950, 1880, 1978, 2200, 2100} };

# implementa un método mostrarPrimeraFila(int[][] tabla) que muestre por pantalla los valores de la
# primera fila de la tabla multidimensional.