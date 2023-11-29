print('Que desea hacer?\n')
print('1- Ingreso')         # menu de opciones
print('2- Reintegro')
print('----------------')

saldo = 0

while True:
    eleccion_usuario = input('\nIngrese una opcion a realizar.(Cualquier otra finaliza el programa.): ')
    if eleccion_usuario in ['1','2']:
        if eleccion_usuario == '1':
            dinero_ingresado = input('Por favor ingrese el dinero: ')
            if dinero_ingresado.isdigit():
                saldo += int(dinero_ingresado)
                print(f'Saldo: {saldo}')
        if eleccion_usuario == '2':
            reintegro_dinero = input('Ingrese el dinero a retirar: ')
            if reintegro_dinero.isdigit():
                saldo -= int(reintegro_dinero)
                print(f'Saldo: {saldo}')
            if int(reintegro_dinero) > saldo:
                print('Saldo insuficiente. Intente nuevamente.')
    else:
        print('Programa finalizado.')
        break