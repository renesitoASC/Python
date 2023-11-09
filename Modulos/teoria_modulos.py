# LOS MODULOS EN PYTHON SON TODOS LOS ARCHIVOS QUE TENGAN LA EXTENSION .py.
# Con los modulos podemos acceder a sus funciones,varibales,objetos,listas etc. PODEMOS ACCEDER A TODO DESDE OTROS MODULOS. 

# Cambiando de nombre un modulo en especifico con "as"
import ejemplo as cambiando_nombre_al_modulo

# Ahora podemos importar un modulo y seleccionar QUE queremos importar nosotros mismos.(Se pueden importar varias cosas.)
from ejemplo import saludar,Saludar,Segundo_saludo  # Tambien podemos cambiarle el nombre a las funciones/variables o lo que hayamos importado
                                                    # Con "as"

saludo_desde_modulo_main = Saludar('rene')  # Creamos una variable y le asignamos la funcion Saludar(parametro) para luego poder mostrarlo
segundo_saludo_desde_modulo_main = Segundo_saludo('franco') # Creamos una variable y le asignamos la funcion Segundo_saludo(parametro) para luego poder mostrarlo

print(saludar)  # Imprimimos la variable "saludar" desde el modulo "ejemplo.py"

# Accedemos al nombre del modulo actual
print(__name__)

# Accedemos al nombre del modulo llamado. (Nombre original, sin tener en cuenta si lo cambiamos con un "as")
# print(ejemplo.__name__)

# Si el modulo estuviera en una carpeta dentro de la misma ruta se importa asi:
from ejemplo01.Modulo01 import ASC  
club_grande = ASC() # Asigno a una variable la funcion ASC()
print(club_grande) 

# Pero si el modulo esta en una carpeta fuera de la misma ruta se hace asi:
import sys  # "sys" es un modulo de python de tipo 'built in'
print(sys.path) # Con este metodo entramos a ver todas las rutas de los modulos. La primer ruta que nos devuelve es la ruta actual

# Ahora para agregar un modulo que esta en otra ruta se hace asi:
sys.path.append('c:\\Users\\frank\\OneDrive\\Escritorio\\Python\\Practica_modulo')  # Luego de este metodo ya esta agregada la carpeta fuera de la misma ruta de la actual
                                                                                    # Y podemos acceder a cualquiera de sus propiedades. Como por ejemplo:  
import modulo_fuera_de_ruta as m_variable   # Aunque este subrayado el programa corre igual y esta bien programado. Luego del import lo que se ingresa es el nombre del modulo.
                                            # NO DE LA CARPETA. QUE YA SE INGRESO EN EL METODO .APPEND() ARRIBA
print(m_variable.variable_ejemplo)  # SIEMPRE que querramos accedere a cualquiera de sus propiedades de un modulo tenemos que hacerlo como si fuera un metodo.
                                    # Donde primero se ingresa el nombre del modulo, seguido de un punto y el nombre de la propiedad.


