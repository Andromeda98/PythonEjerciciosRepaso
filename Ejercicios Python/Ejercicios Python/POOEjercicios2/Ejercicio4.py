class Empleado:
    def __init__(self, nombre=None):  # Constructor por defecto y con parámetros
        self._nombre = nombre
    
    # Getter
    def get_nombre(self):
        return self._nombre
    
    # Setter
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    # toString
    def __str__(self):
        return f"Empleado {self._nombre}"


class Operario(Empleado):
    def __init__(self, nombre=None):
        super().__init__(nombre)
    
    def __str__(self):
        return f"Empleado {self._nombre} -> Operario"


class Directivo(Empleado):
    def __init__(self, nombre=None):
        super().__init__(nombre)
    
    def __str__(self):
        return f"Empleado {self._nombre} -> Directivo"


class Oficial(Operario):
    def __init__(self, nombre=None):
        super().__init__(nombre)
    
    def __str__(self):
        return f"Empleado {self._nombre} -> Operario -> Oficial"


class Tecnico(Operario):
    def __init__(self, nombre=None):
        super().__init__(nombre)
    
    def __str__(self):
        return f"Empleado {self._nombre} -> Operario -> Tecnico"


# Programa de prueba
if __name__ == "__main__":
    # Probando todas las clases
    empleado = Empleado("Juan")
    operario = Operario("Pedro")
    directivo = Directivo("Ana")
    oficial = Oficial("Luis")
    tecnico = Tecnico("Maria")
    
    print(empleado)    # Empleado Juan
    print(operario)    # Empleado Pedro -> Operario
    print(directivo)   # Empleado Ana -> Directivo
    print(oficial)     # Empleado Luis -> Operario -> Oficial
    print(tecnico)     # Empleado Maria -> Operario -> Tecnico
    
    # Probando constructor por defecto
    empleado2 = Empleado()
    empleado2.set_nombre("Carlos")
    print(empleado2)   # Empleado Carlos