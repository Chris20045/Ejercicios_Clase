class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        return self.stock >= cantidad

    def vender(self, cantidad):
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f" Venta realizada: {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}.")
        else:
            print(f" No hay suficiente stock para vender {cantidad} unidades de {self.nombre}.")

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f" Se han agregado {cantidad} unidades de {self.nombre}. Stock total: {self.stock}.")


producto1 = Producto("Laptop", 1200, 10)

print("¿Hay 5 unidades disponibles?", producto1.verificar_disponibilidad(5))
producto1.vender(3)
print("¿Hay 8 unidades disponibles?", producto1.verificar_disponibilidad(8))
producto1.vender(8)  # Intento fallido
producto1.reabastecer(10)
print("¿Hay 8 unidades disponibles?", producto1.verificar_disponibilidad(8))
producto1.vender(8)
