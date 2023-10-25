producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))

total = precio * unidades

print(f'{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€')


# Utilizo el : en este caso para formatear los valores de las diferentes variables, ya sea a flotantes o enteros. Seguidos a los dos puntos esta el numero de caracteres
# que debe mostrar el programa a la hora de correrlo, y dsp de eso esta el .2f que es la cantidad de decimales que debe tener un valor flotante.

