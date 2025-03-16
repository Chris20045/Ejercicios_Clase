class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_informacion(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Numero de paginas: {self.paginas}")

    def actualizar_paginas(self, nuevas_paginas):
        if nuevas_paginas > 0:
            self.paginas = nuevas_paginas
            print(f"El numero de paginas se ha actualizado a {self.paginas}.")
        else:
            print("El numero de páginas debe ser mayor que cero.")

libro1 = Libro("Habitos Atomicos", "James Clear", 320)
libro1.mostrar_informacion()

libro1.actualizar_paginas(240)
libro1.mostrar_informacion()
