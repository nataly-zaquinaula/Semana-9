class Producto:
    def __init__(self, codigo, nombre, categoria, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
        # Devuelve un texto con los datos del producto, listo para imprimir
        return (
            "Codigo: " + self.codigo +
            " | Nombre: " + self.nombre +
            " | Categoria: " + self.categoria +
            " | Precio: $" + str(self.precio)
        )