# Los metodos en python se escriben de la siguiente manera: DATO.METODO()
#Para saber todos los metodos que existen dependiendo del TIPO de dato se utiliza la funcion dir(dato*)

cadena1 = "hola como estas"

# Transcribirlo todo a mayusculas
texto_a_mayus = cadena1.upper()

# Transcribirlo a minusculas
texto_a_minus = cadena1.lower()

# Escribir la primera letra en mayusculas
primera_letra_mayus = cadena1.capitalize()

# Buscamos una cadena en otra cadena, si no la encuentra devuelve -1
busqueda_de_cadena = cadena1.find('h')

# Buscamos una cadena en otra cadena, si no la encuentra devuelve una excepcion
busqueda_de_cadena_excepcion = cadena1.index('h') 

# Si es numerico devuelve True, sino False
es_numerico = cadena1.isnumeric()

# Si es alfanumerico devuelve True, sino False
es_alfanumerico = cadena1.isalpha()

# Contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count('h')

#Contamos cuantos caracteres tiene la cadena
contar_caracteres = len(cadena1)

# Verificamos si una cadena empieza con otra cadena dada (en el parametro), si es asi devuelve True
empeieza_con = cadena1.startswith('h')

# Verificamos si una cadena termina con otra cadena dada (en el parametro), si es asi devuelve True
termina_con = cadena1.endswith('h')

# Si el valor 1 se encuentra en la cadena se reemplaza por lo que haya en el valor 2
reemplazar_con = cadena1.replace('h','H')

# Separamos cadenas que le pasemos
separando_cadenas = cadena1.split('h')

print(es_alfanumerico)

