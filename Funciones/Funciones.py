# Creando una funcion, con la palabra reservada def, luego el nombre de la funcion con los parentesis, dos puntos y luego el cuerpo de la funcion.(Puedo agregar o no parametros)
def Saludar():
    print("Hola mundo!")

# Creando una funcion con parametros
def saludos(nombre,sexo):
    sexo = sexo.lower()
    if sexo == 'mujer':
        adjetivo = 'Reina'
        print(f'Hola {nombre}, como estas {adjetivo}.')
    elif sexo == 'hombre':
        adjetivo = 'idolo'
        print(f'Hola {nombre}, como estas {adjetivo}.')
    else:
        adjetivo = 'puto'
        print(f'Hola {nombre}, como estas {adjetivo}.')

saludos('Rene','Hombre')

# Creando una funcion que nos devuelva valores
def crear_contrasena_random(num):
    chars = 'abcdefghij'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    return contrasena,num       # Aca lo que hacemos con el return es que devolvemos la contrasena, asi luego la podemos almacenar en una variable y trabajar con ella.
                            # Si hubiesemos usado print, se imprimiria y luego dejaria de existir.

# Desempaquetando la funcion
password,numero_usado = crear_contrasena_random(3)

# Mostrando los resultados obtenidos y los datos utilizados.
print(f'Tu contrasena nueva es: {password}')
print(f'El numero que se utilizo fue: {numero_usado}')



