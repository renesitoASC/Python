diccionario = {
    'nombre': 'rene',
    'apellido': 'ASC',
    'edad': 19
}

# Al escribirlo de esta manera siempre me va a devolver la key, sin importar lo que escriba luego del for
for key in diccionario:
    print(key)
    
# Esta es la manera correcta de iterar un diccionario
for dato in diccionario.items():
    key = dato[0]
    valor = dato[1]
    print(f'La llave es: {key} y su valor es: {valor}')
