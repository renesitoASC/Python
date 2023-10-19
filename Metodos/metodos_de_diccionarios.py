Diccionario = {
    'Nombre' : 'Franco',
    'Apellido' : 'Cerana',
    'edad' : 19
}

# Muestra las llaves del diccionario 
claves_con_keys = Diccionario.keys()

# Muestra el valor de una clave del diccionario 
valor_de_llave = Diccionario.get('Nombre')

# Elimina todos los elementos del diccionario
# eliminando_elementos = Diccionario.clear()

# Elimina UN elemento del diccionario (LLAVE Y VALOR)
Diccionario.pop('Nombre')

# Obtiene un elemento dict_items iterable (para poder recorrer el diccionario)
diccionario_iterable = Diccionario.items()

print(diccionario_iterable)