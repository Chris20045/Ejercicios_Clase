class Articulo:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Inventario:
    def __init__(self):
        self.articulos = []

    def agregar_articulo(self, articulo):
        self.articulos.append(articulo)

    def eliminar_articulo(self, articulo):
        if articulo in self.articulos:
            self.articulos.remove(articulo)

    def listar_articulos(self):
        for articulo in self.articulos:
            print(f"Código: {articulo.codigo}, Nombre: {articulo.nombre}, Cantidad: {articulo.cantidad}, Precio: {articulo.precio}")
