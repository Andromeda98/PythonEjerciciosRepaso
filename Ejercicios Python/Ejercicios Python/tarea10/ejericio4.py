# Tabla multidimensional de kilogramos vendidos
kilos = [
    [5, 6, 9, 23, 7, 14, 0],    # Peras - ventas por día de la semana
    [16, 8, 4, 33, 15, 21, 2]   # Manzanas - ventas por día de la semana
]

# Nombres de las frutas
frutas = ["Pera", "Manzana"]

# Precios por kilogramo
precios = [6, 7]  # 6€/kg peras, 7€/kg manzanas

# Sumar cada fila
total_peras = sum(kilos[0])
total_manzanas = sum(kilos[1])


#Pera -&gt; 64 kg x 6€ = 384€
#Manzana -&gt; 99 kg x 7€ = 693€
print(f"{frutas[0]} -> {total_peras}kg x {precios[0]}€ = {total_peras*precios[0]}€" )
print(f"{frutas[1]} -> {total_manzanas}kg x {precios[1]}€ = {total_manzanas*precios[1]}€" )