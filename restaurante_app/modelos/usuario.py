class Usuario:
    def __init__(self, identificacion, nombre, correo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def mostrar_informacion(self):
        return (
            "Identificacion: " + self.identificacion +
            " | Nombre: " + self.nombre +
            " | Correo: " + self.correo
        )