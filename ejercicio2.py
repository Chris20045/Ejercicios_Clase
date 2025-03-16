class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Calificación: {self.calificacion}")

    def verificar_aprobacion(self):
        if self.calificacion >= 3.0:
            print(f"{self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} ha reprobado.")


estudiante1 = Estudiante("Cristofer Calderon", 22, 4.5)
estudiante2 = Estudiante("Roxana Palmar", 19, 2.8)


estudiante1.mostrar_informacion()
estudiante1.verificar_aprobacion()

print("\n")

estudiante2.mostrar_informacion()
estudiante2.verificar_aprobacion()
