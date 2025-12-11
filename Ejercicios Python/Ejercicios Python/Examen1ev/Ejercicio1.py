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


alfabeto = ["A", "B", "C", "D", "E", "F", "G",
            "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P",
            "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]   

mensaje = "este mensaje es secreto"

clave = 3

texto_cifrado = ""

for letra in mensaje.upper():
    if letra in alfabeto:
        posicion = alfabeto.index(letra)
        posicion = (posicion + clave)
        if posicion >= len(alfabeto):
            nueva_posicion = posicion - len(alfabeto)
        else:
            nueva_posicion = posicion
        texto_cifrado += alfabeto[nueva_posicion]
    else:
        texto_cifrado += letra  

print("Mensaje cifrado:", texto_cifrado)








