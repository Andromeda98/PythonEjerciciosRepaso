import random

class Persona:

     # Constructor por defecto
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.dni = ""
        self.sexo = 'H'  # H por defecto
        self.peso = 0.0
        self.altura = 0.0

    # Constructor con nombre, edad y sexo (resto por defecto)
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.dni = ""
        self.peso = 0.0
        self.altura = 0.0
        
    def __init__(self, nombre="", edad=0, dni="", sexo='H', peso=0.0, altura=0.0):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni if dni else self.generar_dni()  # Si no hay DNI, generar uno
        self.sexo = self.validar_sexo(sexo)  # Validar sexo
        self.peso = peso
        self.altura = altura

    def validar_sexo(self, sexo):
        """Valida que el sexo sea 'H' o 'M'"""
        if sexo.upper() in ['H', 'M']:
            return sexo.upper()
        else:
            print(f"❌ Sexo '{sexo}' no válido. Se usará 'H' por defecto.")
            return 'H'

    def generar_dni(self):
        """Genera un DNI válido con número y letra según tabla oficial"""
        # Tabla oficial de letras para DNI
        letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
        
        # Generar número de 8 dígitos
        numero = random.randint(10000000, 99999999)
        
        # Calcular letra correspondiente
        resto = numero % 23
        letra = letras_dni[resto]
        
        # Formatear con ceros a la izquierda si es necesario
        dni_generado = f"{numero:08d}{letra}"
        return dni_generado

    # Getters
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_dni(self):
        return self.dni
    
    def get_sexo(self):
        return self.sexo
    
    def get_peso(self):
        return self.peso
    
    def get_altura(self):
        return self.altura

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_edad(self, edad):
        self.edad = edad
    
    def set_dni(self, dni):
        self.dni = dni
    
    def set_sexo(self, sexo):
        self.sexo = self.validar_sexo(sexo)
    
    def set_peso(self, peso):
        self.peso = peso
    
    def set_altura(self, altura):
        self.altura = altura

    def __str__(self):
        return (f"Persona: [Nombre: {self.nombre}, Edad: {self.edad}, "
                f"DNI: {self.dni}, Sexo: {self.sexo}, Peso: {self.peso}kg, "
                f"Altura: {self.altura}m]")