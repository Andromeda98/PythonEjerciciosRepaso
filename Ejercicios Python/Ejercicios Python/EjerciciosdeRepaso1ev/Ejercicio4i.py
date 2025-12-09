def eliminar_caracteres(texto):
    # Eliminar todas las 'b'
    texto_sin_b = texto.replace('b', '')
    # Eliminar todas las 'ac'
    texto_final = texto_sin_b.replace('ac', '')
    return texto_final

# Ejemplo de uso
texto_original = "python"
resultado = eliminar_caracteres(texto_original)
print(f"Texto original: '{texto_original}'")
print(f"Texto modificado: '{resultado}'")