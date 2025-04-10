class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        nueva_velocidad = self.velocidad_actual + incremento
        if nueva_velocidad > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
        else:
            self.velocidad_actual = nueva_velocidad
        print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def frenar(self, decremento):
        nueva_velocidad = self.velocidad_actual - decremento
        if nueva_velocidad < 0:
            self.velocidad_actual = 0
        else:
            self.velocidad_actual = nueva_velocidad
        print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def verificar_limite(self, velocidad_limite):
        if self.velocidad_actual > velocidad_limite:
            print(f"El vehículo excede el límite de velocidad de {velocidad_limite} km/h.")
        else:
            print(f"El vehículo está dentro del límite de velocidad de {velocidad_limite} km/h.")



def menu():
    print("=== Sistema de Monitoreo de Velocidad ===")
    marca = input("Ingresa la marca del vehículo: ")
    modelo = input("Ingresa el modelo del vehículo: ")
    velocidad_maxima = int(input("Ingresa la velocidad máxima del vehículo (km/h): "))

    vehiculo = Vehiculo(marca, modelo, velocidad_maxima)

    while True:
        print("\nMenú ")
        print("1. Acelerar")
        print("2. Frenar")
        print("3. Verificar límite de velocidad")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            incremento = int(input("¿Cuántos km/h deseas acelerar?: "))
            vehiculo.acelerar(incremento)
        elif opcion == "2":
            decremento = int(input("¿Cuántos km/h deseas frenar?: "))
            vehiculo.frenar(decremento)
        elif opcion == "3":
            limite = int(input("Ingresa el límite de velocidad (km/h): "))
            vehiculo.verificar_limite(limite)
        elif opcion == "4":
            print("Saliendo del sistema. ¡Conduce seguro! 🚗")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


menu()
