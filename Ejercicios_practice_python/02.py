numero = int(input('Ingrese un numero: '))
resultado_paridad = numero % 2

if resultado_paridad == 0:
    print('Su numero es par.')
    if numero % 4 == 0:
        print('Y tambien es multiplo de 4')
else:
    print('Su numero es impar.')

numero_dividendo = int(input('\nIngrese un dividendo: '))
numero_divisior = int(input('Ingrese su divisor: '))

if numero_dividendo % numero_divisior == 0:
    print('El resto es 0. Fin del programa')
else:
    print('El resto NO es 0. Fin del programa')