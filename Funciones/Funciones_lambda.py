numeros = [1,2,3,4,5,6,7,8,9]

# Creando una funcion lamba para multiplicar por dos
multiplicar_por_dos = lambda x : x*2

# Creando una funcion que diga si es par o no
def es_par(num):
    if (num%2==0):
        return True
    
# Usando filter con una funcion comun
numeros_pares = filter(lambda numero:numero%2 == 0,numeros)  # Lo que hace la funcion filter es que crea una lista con todos los valores que devuelvan True de una lista


# Creando lo mismo que antes pero con lambda

print(list(numeros_pares))