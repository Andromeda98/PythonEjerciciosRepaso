for indice in range(1, 111):
    # Verificar múltiplos
    if indice % 3 == 0 and indice % 5 == 0:
        print("CozaLoza", end=" ")
    elif indice % 3 == 0:
        print("Coza", end=" ")
    elif indice % 5 == 0:
        print("Loza", end=" ")
    elif indice % 7 == 0:
        print("Woza", end=" ")
    else:
        print(indice, end=" ")
    
    # Salto de línea cada 11 números
    if indice % 11 == 0:
        print()  # Esto hace el salto de línea