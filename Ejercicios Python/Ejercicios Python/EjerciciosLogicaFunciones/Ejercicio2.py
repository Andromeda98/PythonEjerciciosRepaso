from datetime import date

def contador_nochebuena_datetime():
    print("¡Bienvenido al Contador Regresivo para Nochebuena!")
    print("=" * 60)
    
    # Solicitar fecha actual al usuario
    print("Ingresa la fecha actual.")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))
    
    # Crear objetos de fecha
    fecha_actual = date(año, mes, dia)
    nochebuena = date(año, 12, 24)
    
    # Calcular diferencia
    if fecha_actual <= nochebuena:
        dias_faltantes = (nochebuena - fecha_actual).days
        print(f"\nFaltan {dias_faltantes} días para Nochebuena. ¡La Navidad está cerca!")
    else:
        # Si ya pasó Navidad, calcular para el próximo año
        nochebuena_proximo = date(año + 1, 12, 24)
        dias_faltantes = (nochebuena_proximo - fecha_actual).days
        print(f"\n¡Ya pasó Navidad! Faltan {dias_faltantes} días para la próxima Nochebuena.")

# Ejecutar programa
contador_nochebuena_datetime()