# Creando diccionarios con dict()
diccionario = dict(nombre="Franco",apellido="Cerana")

# las listas no pueden ser claves y utilizamos "frozenset" para meter conjuntos
diccionario = {frozenset(["franco","cerana"]): "jaja"}

# Creando diccionarios con "fromkeys". Lo que hacemos aca es crear diccionarios con keys de valores indefinidos.
diccionario = dict.fromkeys(["Nombre","Apellido"],"Club")



print(diccionario)