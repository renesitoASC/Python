# Forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,3,9,10,20,3])

# Lo mismo que arriba pero utilizando el operador * como parametro (args)
def suma (nombre,*numeros):  # El parametro args toma valores infinitos, por eso siempre que lo vayamos a utilizar (en los parentesis) tiene que ir como ultimo parametro junto a su variable.
    return f'{nombre}, la suma de tus numeros es: {sum(numeros)}'

resultado = suma('Rene',5,9,3,10,20,3)

print(resultado)