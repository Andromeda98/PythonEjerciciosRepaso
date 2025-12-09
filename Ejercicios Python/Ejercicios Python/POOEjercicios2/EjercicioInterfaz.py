from abc import ABC, abstractmethod
from typing import List

# Interfaz Vehículo
class Vehiculo(ABC):
    def __init__(self):
        self._velocidad = 0
    
    @abstractmethod
    def frenar(self, cuanto: int) -> str:
        pass
    
    @abstractmethod
    def acelerar(self, cuanto: int) -> str:
        pass

# Clase Coche
class Coche(Vehiculo):
    def __init__(self, color: str, plazas: int):
        super().__init__()
        self._color = color
        self._plazas = plazas
    
    def frenar(self, cuanto: int) -> str:
        self._velocidad = max(0, self._velocidad - cuanto)
        return f"Coche {self._color} frenando {cuanto} km/h. Velocidad actual: {self._velocidad} km/h"
    
    def acelerar(self, cuanto: int) -> str:
        self._velocidad += cuanto
        return f"Coche {self._color} acelerando {cuanto} km/h. Velocidad actual: {self._velocidad} km/h"
    
    def getPlazas(self) -> int:
        return self._plazas
    
    def getColor(self) -> str:
        return self._color
    
    def __str__(self) -> str:
        return f"Coche - Color: {self._color}, Plazas: {self._plazas}, Velocidad: {self._velocidad} km/h"

# Clase Moto
class Moto(Vehiculo):
    def __init__(self, cilindrada: int):
        super().__init__()
        self._cilindrada = cilindrada
    
    def frenar(self, cuanto: int) -> str:
        self._velocidad = max(0, self._velocidad - cuanto)
        return f"Moto {self._cilindrada}cc frenando {cuanto} km/h. Velocidad actual: {self._velocidad} km/h"
    
    def acelerar(self, cuanto: int) -> str:
        self._velocidad += cuanto
        return f"Moto {self._cilindrada}cc acelerando {cuanto} km/h. Velocidad actual: {self._velocidad} km/h"
    
    def getCilindrada(self) -> int:
        return self._cilindrada
    
    def __str__(self) -> str:
        return f"Moto - Cilindrada: {self._cilindrada}cc, Velocidad: {self._velocidad} km/h"

# Método main
def main():
    # Crear ArrayList (lista en Python) con 3 coches y 2 motos
    vehiculos: List[Vehiculo] = [
        Coche("Rojo", 5),
        Coche("Azul", 4),
        Coche("Verde", 7),
        Moto(600),
        Moto(1000)
    ]
    
    print("=== INICIALIZACIÓN DE VEHÍCULOS ===")
    for vehiculo in vehiculos:
        print(vehiculo)
    
    print("\n" + "="*50)
    print("=== PROBANDO MÉTODOS ACELERAR ===")
    # Probar acelerar en todos los vehículos
    for i, vehiculo in enumerate(vehiculos):
        print(f"\nVehículo {i + 1}:")
        print(vehiculo.acelerar(30))
        print(vehiculo.acelerar(20))
    
    print("\n" + "="*50)
    print("=== PROBANDO MÉTODOS FRENAR ===")
    # Probar frenar en todos los vehículos
    for i, vehiculo in enumerate(vehiculos):
        print(f"\nVehículo {i + 1}:")
        print(vehiculo.frenar(15))
        print(vehiculo.frenar(10))
    
    print("\n" + "="*50)
    print("=== PROBANDO MÉTODOS ESPECÍFICOS ===")
    # Probar métodos específicos de cada clase
    for i, vehiculo in enumerate(vehiculos):
        print(f"\nVehículo {i + 1}:")
        print(vehiculo)
        
        if isinstance(vehiculo, Coche):
            print(f"  - Plazas: {vehiculo.getPlazas()}")
            print(f"  - Color: {vehiculo.getColor()}")
        elif isinstance(vehiculo, Moto):
            print(f"  - Cilindrada: {vehiculo.getCilindrada()}cc")
    
    print("\n" + "="*50)
    print("=== ESTADO FINAL DE TODOS LOS VEHÍCULOS ===")
    for i, vehiculo in enumerate(vehiculos):
        print(f"{i + 1}. {vehiculo}")

# Ejecutar el programa
if __name__ == "__main__":
    main()

    