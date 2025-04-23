
class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.__sueldo_base = sueldo_base  # atributo privado

  
    def get_sueldo_base(self):
        return self.__sueldo_base

    
    def set_sueldo_base(self, nuevo_sueldo):
        if nuevo_sueldo > 0:
            self.__sueldo_base = nuevo_sueldo
        else:
            print("El sueldo debe ser mayor que 0.")

    
    def calcular_salario(self):
        return self.__sueldo_base


class EmpleadoFijo(Empleado):
    def calcular_salario(self):
        return self.get_sueldo_base() + 500  


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, sueldo_base, horas_trabajadas, valor_hora):
        super().__init__(nombre, sueldo_base)
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.valor_hora

class EmpleadoTemporal(Empleado):
    def calcular_salario(self):
        return self.get_sueldo_base() * 0.9  


empleados = [
    EmpleadoFijo("Cristofer", 1200),
    EmpleadoPorHoras("David", 0, 40, 15),
    EmpleadoTemporal("Calderon", 1000)
]


for emp in empleados:
    print(f"{emp.nombre}: ${emp.calcular_salario():.2f}")
