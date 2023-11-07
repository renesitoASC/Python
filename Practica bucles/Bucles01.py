contraseña_establecida = 'ASC'
ingresar_contraseña = ''

while ingresar_contraseña != contraseña_establecida:
    ingresar_contraseña = input('\nIngrese la contraseña: ')
    if ingresar_contraseña != contraseña_establecida:
        print('Contraseña incorrecta. Intente nuevamente.')

print('Contraseña correcta.')