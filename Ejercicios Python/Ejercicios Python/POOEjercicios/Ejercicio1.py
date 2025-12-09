class Cuenta:
    # Constructor con cantidad opcional
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    # Getters
    def get_titular(self):
        return self.titular

    def get_cantidad(self):
        return self.cantidad

    # Setters
    def set_titular(self, titular):
        self.titular = titular

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad  # ¡Falta el = para asignar!
        # Si es negativa, no hacemos nada (como pide el ejercicio)

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
            # Si queda negativo, ponemos a 0
            if self.cantidad < 0:
                self.cantidad = 0

    # Método toString (en Python se usa __str__)
    def __str__(self):
        return f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}€"
    

def main():
    print("=== DEMOSTRACIÓN CLASE CUENTA ===")
    
    # Crear cuentas
    cuenta1 = Cuenta("Juan Pérez", 1000.0)
    cuenta2 = Cuenta("María García")  # Cantidad por defecto 0.0
    
    print("\n--- Estado inicial ---")
    print(cuenta1)
    print(cuenta2)
    
    print("\n--- Operaciones cuenta1 ---")
    cuenta1.ingresar(500.0)    # ✅ Ingreso positivo
    cuenta1.ingresar(-100.0)   # ❌ Ingreso negativo (no hace nada)
    cuenta1.retirar(200.0)     # ✅ Retiro normal
    cuenta1.retirar(2000.0)    # ❌ Retiro mayor al saldo (pone a 0)
    
    print("\n--- Operaciones cuenta2 ---")
    cuenta2.ingresar(300.0)
    cuenta2.retirar(50.0)
    
    print("\n--- Estado final ---")
    print(cuenta1)
    print(cuenta2)

if __name__ == "__main__":
    main()