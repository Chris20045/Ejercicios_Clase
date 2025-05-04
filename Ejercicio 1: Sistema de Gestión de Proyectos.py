class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(f"Empleado: {empleado.nombre}")

class Empleado:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.proyectos = []

    def asignar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
        proyecto.agregar_empleado(self)
