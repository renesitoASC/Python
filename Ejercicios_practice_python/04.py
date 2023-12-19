numero = int(input('Ingrese un numero: '))
lista_divisores = []

for num in range(1,numero+1):
    if numero % num == 0:
        lista_divisores.append(num)
    else:
        pass

print('Los divisores son: ' + str(lista_divisores))