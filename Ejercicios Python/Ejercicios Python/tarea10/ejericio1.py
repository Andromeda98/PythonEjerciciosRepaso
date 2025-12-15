# Tarea 10: Ejercicios

# Ejercicio 1: Tenemos la siguiente tabla multidimensional, la cual almacena
# por cada una de sus filas el salario trimestral de cada uno de los
# empleados de la empresa:
# int salarios[][] = { {700, 900, 1300} , {1000, 950, 1080}, {1300, 930, 1200} }
# A su vez, disponemos también de una tabla empleados, con los nombres
# de los trabajadores:
# String empleados[] = {&quot;Javier Marías&quot;, &quot;Antonio Muñoz&quot;, &quot;Isabel Allende&quot;}
# Implementa un programa Java que muestre por pantalla lo siguiente:

# Javier Marías -&gt; 700 + 900 + 1300 = 2900€
# Antonio Muñoz -&gt; 1000 + 950 + 1080 = 3030€
# Isabel Allende -&gt; 1300 + 930 + 1200 = 3430€

# Ejercicio 2: Utilizando las mismas tablas del ejercicio anterior,
# implementa un programa Java que ordene los salarios de cada uno de los
# empleados de mayor a menor, y los muestre ordenados por pantalla de la
# siguiente forma:

# Javier Marías -&gt; 700 / 900 / 1300
# Antonio Muñoz -&gt; 950 / 1000 / 1080
# Isabel Allende -&gt; 930 / 1200 / 1300
# Ejercicio 3: Tenemos la siguiente tabla multidimensional:
# int tabla[][] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};

# Implementa un método Java llamado “modificar” que, dado una tabla
# multidimensional y un entero positivo, multiplique todos los elementos
# de dicha tabla por el entero dado. Al finalizar la operación, deberás
# mostrar el resultado de final de la tabla en el método main.

# 2
# Ejercicio 4: Tenemos la siguiente tabla multidimensional, la cual almacena
# por cada una de sus filas el número de kilogramos vendidos de peras y
# manzanas en una frutería:

# int kilos[][] = {{5, 6, 9, 23, 7, 14, 0}, {16, 8, 4, 33, 15, 21, 2}};

# A su vez, disponemos también de una tabla alimentos, con los nombres
# de las dos frutas de temporada que estamos vendiendo:
# String frutas[] = {&quot;Pera&quot;, &quot;Manzana&quot;}
# Y una tabla con los precios de ambos alimentos:
# int precios[] = {6, 7};

# Implementa un programa Java que te muestre la suma total de los
# kilogramos vendidos de cada uno de los alimentos, y al final muestre las
# ganancias obtenidas gracias a las ventas de cada uno de ellos. El resultado
# debe ser el siguiente:

# Pera -&gt; 64 kg x 6€ = 384€
# Manzana -&gt; 99 kg x 7€ = 693€

# Ejercicio 5: Tenemos la siguiente tabla:

# String nombres[] = {&quot;Pepe&quot;, &quot;Juan&quot;, &quot;María&quot;, &quot;Antonio&quot;, &quot;Luisa&quot;};

# Implementa un programa Java que ordene la tabla anterior
# alfabéticamente, y muestre el resultado final por pantalla.





numeros = [2,4,6,77,8,4]

print(sum(numeros))


def calcular_suma(lista_numeros):
    """
    Calcula la suma de una lista de números.
    
    Args:
        lista_numeros (list): Lista de números
        
    Returns:
        int/float: La suma de los números
    """
    return sum(lista_numeros)

# Ejemplo de uso
numeros = [2, 4, 6, 77, 8, 4]
suma_total = calcular_suma(numeros)
print(f"La suma de {numeros} es: {suma_total}")