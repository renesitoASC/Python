# LOS MODULOS EN PYTHON SON TODOS LOS ARCHIVOS QUE TENGAN LA EXTENSION .py.
# Con los modulos podemos acceder a sus funciones,varibales,objetos,listas etc. PODEMOS ACCEDER A TODO DESDE OTROS MODULOS. 

# Cambiando de nombre un modulo en especifico con "as"
#import ejemplo as cambiando_nombre_al_modulo

# Ahora podemos importar un modulo y seleccionar QUE queremos importar nosotros mismos.(Se pueden importar varias cosas.)
from ejemplo import saludar,Saludar,Segundo_saludo,saludar

saludo_desde_modulo_main = Saludar('rene')  # Creamos una variable y le asignamos la funcion Saludar(parametro) para luego poder mostrarlo
segundo_saludo_desde_modulo_main = Segundo_saludo('franco') # Creamos una variable y le asignamos la funcion Segundo_saludo(parametro) para luego poder mostrarlo

print(saludar)  # Imprimimos la variable "saludar" desde el modulo "ejemplo.py"

# Accedemos al nombre del modulo actual
print(__name__)

# Accedemos al nombre del modulo llamado. (Nombre original, sin tener en cuenta si lo cambiamos con un "as")
# print(ejemplo.__name__)

