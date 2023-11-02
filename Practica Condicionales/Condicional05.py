edad_cliente_ingresada = int(input('Por favor ingrese la edad del cliente: '))

if edad_cliente_ingresada < 4:
    print('Puede ingresar gratis.')
elif edad_cliente_ingresada > 4 and edad_cliente_ingresada < 18:
    print('La entrada es 5 eur.')
elif edad_cliente_ingresada > 18:
    print('Tiene que pagar 10 eur.')

