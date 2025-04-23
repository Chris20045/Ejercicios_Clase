
class Transporte:
    def tipo_transporte(self):
        print("Tipo de transporte no especificado")


class Coche(Transporte):
    def tipo_transporte(self):
        print("Transporte terrestre")

class Avion(Transporte):
    def tipo_transporte(self):
        print("Transporte aéreo")

class Barco(Transporte):
    def tipo_transporte(self):
        print("Transporte marítimo")


def mostrar_tipo(transporte):
    transporte.tipo_transporte()

t1 = Coche()
t2 = Avion()
t3 = Barco()


mostrar_tipo(t1)
mostrar_tipo(t2)
mostrar_tipo(t3)
