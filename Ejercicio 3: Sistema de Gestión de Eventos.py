class Evento:
    def __init__(self, nombre, fecha, ubicacion):
        self.nombre = nombre
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.participantes = []

    def agregar_participante(self, persona):
        self.participantes.append(persona)

    def mostrar_participantes(self):
        for participante in self.participantes:
            print(f"Participante: {participante.nombre}, Email: {participante.email}")

class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
