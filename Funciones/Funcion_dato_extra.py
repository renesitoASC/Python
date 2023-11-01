# Creando una funcion de 3 parametros
def frase1(nombre,apellido,adj):
    return f'Hola {nombre}{apellido} sos muy {adj}'

# Utilizando keywords Arguments
frase_resultante = frase1(adj='capo',nombre='rene',apellido='asc')

# Creando la misma funcion con un parametro opcional y un valor default
def frase2(nombre,apellido,adj='tonto'):   # Aqui cree un parametro opcional y le asigne un valor default, que luego puede ser cambiado a la hora de llamar a la funcion
                                                        # y pasarle otro parametro con otro valor
    return f'Hola {nombre}{apellido}, sos muy {adj}'

frase_resultante2 = frase2('rene','asc','inteligente')
