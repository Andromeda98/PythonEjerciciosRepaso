# Ejercicio 1: En criptografía, el cifrado César, también conocido como cifrado por
# desplazamiento, código de César o desplazamiento de César, es una de las técnicas de cifrado
# más simples y más usadas. Es un tipo de cifrado por sustitución en el que una letra en el texto
# original es reemplazada por otra letra que se encuentra un número fijo de posiciones más
# adelante en el alfabeto. Por ejemplo, con un desplazamiento de 3, la A sería sustituida por la D
# (situada 3 lugares a la derecha de la A), la B sería reemplazada por la E, etc. Este método debe
# su nombre a Julio César, que lo usaba para comunicarse con sus generales.

# El cifrado César mueve cada letra un determinado número de espacios en el alfabeto. En este
# ejemplo se usa un desplazamiento de tres espacios, así que una B en el texto original se
# convierte en una E en el texto codificado.
# Java no dispone de ninguna función nativa que devuelva el abecedario, por lo tanto, para
# facilitar la resolución del problema vamos a utilizar la siguiente tabla que utilizaremos para
# calcular los cambios en las letras de la palabra a cifar:

# String[] abecedario = {"a", "b", "c", "d", "e", "f", "g",
# "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p",
# "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};

# 4 puntos

# Apellidos: Nombre: No.
# Ejercicio 2: viendo el auge de las máquinas de golosinas, el colegio ha decidido invertir en la
# empresa Sabor Dulce el total del presupuesto anual. Los futuros programadores de 1oH-V se
# han dado cuenta que el algoritmo que maneja las máquinas está anticuado, y no siempre
# funciona bien. Por ello, tras unas largas reuniones se ha decidido implementar un nuevo
# software en Java que gestione la compra de productos en las máquinas. El nuevo algoritmo
# mostrará el siguiente mensaje hasta que el usuario escriba fin:

# Y se quedará a la espera de que el usuario introduzca uno de los 3 posibles comandos:
# ● insertar [dinero]: Si el usuario introduce el comando insertar, se añade al sueldo actual
# el valor del dinero introducido. La máquina SÓLO ACEPTA monedas de 1 y 2 euros. Una
# vez introducido el dinero, muestra por pantalla el saldo actual.
# ● retirar [idProducto]: Si el usuario introduce el comando retirar, la máquina entrega al
# usuario el producto cuya id coincide con la [idProducto] seleccionada por el usuario. Si el
# dinero introducido por el usuario NO ES SUFICIENTE, la máquina muestra por consola
# un mensaje de error, indicando cuánto dinero le falta al usuario. Si no ha habido ningún
# problema durante la compra, muestra por pantalla el nombre del producto comprado
# junto al dinero restante que le queda al usuario.
# ● fin: Si el usuario introduce el comando fin, la máquina muestra por consola el dinero
# restante que devolverá al usuario y finaliza el programa.
# La máquina contiene un total de 5 productos (inventados por el programador para realizar las
# pruebas del software diseñado). Estos productos se almacenan en una tabla multidimensional
# String de 5 columnas y 3 filas. En la primera de ellas, se almacena el identificador del producto.
# En la segunda el precio en euros (SOLAMENTE PUEDEN VALER 1 O 2 EUROS), y en la
# tercera fila el nombre completo del producto. Un ejemplo sería el siguiente:
# ID “manzana” “patatas” “galletas”
# Precio “2” “1” “2”
# Nombre “Manzana Golden Verde” “Fritos Matutano” “Galletas Principito”

# 4 puntos

# Ejercicio 3: Dada la siguiente tabla multidimensional, la cual almacena el salario mensual de los
# empleados (cada fila pertenece a un empleado distinto):
# int salarios[][] = { {700, 900, 1300, 800, 790, 850} , {1000, 950, 1080, 1070, 1200, 1100}, {1300,

# 930, 1200, 1170, 1000, 1000} , {1500, 1950, 1880, 1978, 2200, 2100} };

# implementa un método maxFila(int[][] tabla) que devuelve la posición de la fila cuya suma de
# todos sus datos es mayor.