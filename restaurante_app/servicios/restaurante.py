from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    def __init__(self):
        # list: usamos listas porque la cantidad de productos y usuarios
        # va cambiando mientras el programa esta en ejecucion
        self.productos = []
        self.usuarios = []

    # ---------- PRODUCTOS ----------

    def registrar_producto(self, producto):
        # Antes de registrar, revisamos que el codigo no exista ya
        if self.buscar_producto(producto.codigo) is not None:
            print("Error: ya existe un producto con ese codigo.")
            return False

        self.productos.append(producto)
        print("Producto registrado correctamente.")
        return True

    def buscar_producto(self, codigo):
        # Recorremos la lista buscando el codigo indicado
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(self, codigo, nombre, categoria, precio):
        producto = self.buscar_producto(codigo)
        if producto is None:
            print("Error: no existe un producto con ese codigo.")
            return False

        # Solo cambiamos el dato si el usuario escribio algo nuevo
        if nombre != "":
            producto.nombre = nombre
        if categoria != "":
            producto.categoria = categoria
        if precio is not None:
            producto.precio = precio

        print("Producto actualizado correctamente.")
        return True

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)
        if producto is None:
            print("Error: no existe un producto con ese codigo.")
            return False

        self.productos.remove(producto)
        print("Producto eliminado correctamente.")
        return True

    def listar_productos(self):
        if len(self.productos) == 0:
            print("No hay productos registrados.")
            return

        print("\n--- LISTADO DE PRODUCTOS ---")
        for producto in self.productos:
            print(producto.mostrar_informacion())

    def mostrar_categorias(self):
        # set: usamos un conjunto para que las categorias repetidas
        # no aparezcan varias veces
        categorias = set()
        for producto in self.productos:
            categorias.add(producto.categoria)

        if len(categorias) == 0:
            print("No hay categorias registradas todavia.")
            return

        print("\n--- CATEGORIAS REGISTRADAS ---")
        for categoria in categorias:
            print("- " + categoria)

    # ---------- USUARIOS ----------

    def registrar_usuario(self, usuario):
        for u in self.usuarios:
            if u.identificacion == usuario.identificacion:
                print("Error: ya existe un usuario con esa identificacion.")
                return False

        self.usuarios.append(usuario)
        print("Usuario registrado correctamente.")
        return True

    def listar_usuarios(self):
        if len(self.usuarios) == 0:
            print("No hay usuarios registrados.")
            return

        print("\n--- LISTADO DE USUARIOS ---")
        for usuario in self.usuarios:
            print(usuario.mostrar_informacion())