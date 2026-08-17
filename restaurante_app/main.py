from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


# tuple: el texto del menu no cambia mientras el programa corre,
# por eso usamos una tupla en vez de una lista
TEXTO_MENU = (
    "========================================",
    "           SISTEMA DE RESTAURANTE",
    "========================================",
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "----------------------------------------",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "----------------------------------------",
    "8. Mostrar categorias",
    "9. Salir",
)


def mostrar_menu():
    for linea in TEXTO_MENU:
        print(linea)


def registrar_producto(restaurante):
    print("\n--- Registrar producto ---")
    codigo = input("Codigo: ")
    nombre = input("Nombre: ")
    categoria = input("Categoria: ")
    precio_texto = input("Precio: ")

    try:
        precio = float(precio_texto)
    except ValueError:
        print("Error: el precio debe ser un numero.")
        return

    producto = Producto(codigo, nombre, categoria, precio)
    restaurante.registrar_producto(producto)


def buscar_producto(restaurante):
    print("\n--- Buscar producto ---")
    codigo = input("Codigo a buscar: ")
    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("No se encontro ningun producto con ese codigo.")
    else:
        print(producto.mostrar_informacion())


def actualizar_producto(restaurante):
    print("\n--- Actualizar producto ---")
    codigo = input("Codigo del producto a actualizar: ")
    nombre = input("Nuevo nombre (Enter para no cambiar): ")
    categoria = input("Nueva categoria (Enter para no cambiar): ")
    precio_texto = input("Nuevo precio (Enter para no cambiar): ")

    precio = None
    if precio_texto != "":
        try:
            precio = float(precio_texto)
        except ValueError:
            print("Error: el precio debe ser un numero, no se actualizo.")

    restaurante.actualizar_producto(codigo, nombre, categoria, precio)


def eliminar_producto(restaurante):
    print("\n--- Eliminar producto ---")
    codigo = input("Codigo del producto a eliminar: ")
    restaurante.eliminar_producto(codigo)


def listar_productos(restaurante):
    restaurante.listar_productos()


def registrar_usuario(restaurante):
    print("\n--- Registrar usuario ---")
    identificacion = input("Identificacion: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")

    usuario = Usuario(identificacion, nombre, correo)
    restaurante.registrar_usuario(usuario)


def listar_usuarios(restaurante):
    restaurante.listar_usuarios()


def mostrar_categorias(restaurante):
    restaurante.mostrar_categorias()


def main():
    restaurante = Restaurante()

    # dict: cada opcion del menu (clave) se asocia con la funcion
    # que debe ejecutarse (valor). Asi evitamos una cadena larga de if/elif
    acciones = {
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias,
    }

    while True:
        print()
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "9":
            print("\nSaliendo del sistema...")
            break

        funcion = acciones.get(opcion)
        if funcion is None:
            print("\nOpcion invalida, intente de nuevo.")
        else:
            funcion(restaurante)


if __name__ == "__main__":
    main()