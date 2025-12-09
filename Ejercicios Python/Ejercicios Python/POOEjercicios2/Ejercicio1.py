class Triangulo:
    # Constructor por defecto
    def __init__(self, b=0, y=0, j=0, h=0):
        self.b = b  # Lado base
        self.y = y  # Lado 2
        self.j = j  # Lado 3
        self.h = h  # Altura

    def area(self):
        # Fórmula del área: (base * altura) / 2
        return (self.b * self.h) / 2

    def perimetro(self):
        # Suma de los tres lados
        return self.b + self.y + self.j


# Creando triángulos con el constructor con parámetros
triangulo1 = Triangulo(5, 3, 4, 3)
triangulo2 = Triangulo(6, 5, 5, 4)

print("Área del triángulo 1:", triangulo1.area())
print("Perímetro del triángulo 1:", triangulo1.perimetro())

print("Área del triángulo 2:", triangulo2.area())
print("Perímetro del triángulo 2:", triangulo2.perimetro())
