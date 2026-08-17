## Sistema de Restaurante
Estudiante: Nataly Zaquinaula
# Descripcion del sistema
Programa de consola en Python que administra productos y usuarios de un restaurante. Permite registrar, buscar, actualizar, eliminar y listar productos; registrar y listar usuarios; y mostrar las categorias de productos registradas.
# Estructura del proyecto
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md
# Responsabilidad de cada archivo
modelos/producto.py: clase Producto. Guarda codigo, nombre, categoria y precio de un producto.
modelos/usuario.py: clase Usuario. Guarda identificacion, nombre y correo de una persona registrada.
servicios/restaurante.py: clase Restaurante. Administra las listas de productos y usuarios (registrar, buscar, actualizar, eliminar, listar).
main.py: muestra el menu, pide datos por consola y llama a los metodos de Restaurante.
# Estructuras de datos utilizadas
list: self.productos y self.usuarios en Restaurante. Son listas porque la cantidad de productos y usuarios cambia mientras el programa corre.
tuple: TEXTO_MENU en main.py. Es una tupla porque el texto del menu no cambia durante la ejecucion.
dict: acciones en main.py. Asocia cada numero de opcion con la funcion que debe ejecutarse, para no usar una cadena larga de if/elif.
set: dentro de mostrar_categorias() en Restaurante. Se usa un conjunto para mostrar las categorias sin que se repitan.
# Instrucciones de ejecucion
Ubicarse en la carpeta que contiene restaurante_app/.
Ejecutar:
python restaurante_app/main.py
Elegir una opcion del menu (1 al 9) y seguir las instrucciones en pantalla.
# Reflexion
Elegir bien la estructura de datos ayuda a que el codigo sea mas claro. Las listas sirven para colecciones que cambian de tamano, la tupla protege datos que no deben cambiar, el diccionario relaciona una clave con su valor de forma directa, y el conjunto evita duplicados sin que se tenga que revisar manualmente.