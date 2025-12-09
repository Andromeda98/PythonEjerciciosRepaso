class Rectangulo:
    # Constructor por defecto
    def __init__(self, b=0, h=0):
        self.b = b  # Lado base

        self.h = h  # Altura

    def area(self):
        # Fórmula del área: (base * altura) / 2
        return self.b * self.h

    def perimetro(self):
        # Suma de los tres lados
        return (self.b*2) + (self.h*2) 


rectangulo1= Rectangulo(7,3)
rectangulo2= Rectangulo(9,6)
print("Área del triángulo 1:", rectangulo1.area())
print("Perímetro del triángulo 1:", rectangulo1.perimetro())

print("Área del triángulo 2:", rectangulo2.area())
print("Perímetro del triángulo 2:", rectangulo2.perimetro())
