sexo_ingresado = input('Ingrese su sexo: ')
aux_sexo = sexo_ingresado.lower()

nombre_ingresado = input("Ingrese su nombre: ")
aux_nombre = nombre_ingresado.lower()

#print(aux_nombre)       Auxiliares para verificar que los metodos se hayan aplicado y funcionen bien
#print(aux_sexo)

if aux_sexo.startswith('m'):
    if aux_nombre < 'm':
        print('Estas en el grupo A, mamita.')
    else:
        print('Estas en el grupo B, mamita.')

if aux_sexo.startswith('h'):
    if aux_nombre > 'n':
        print('Estas en el grupo A, pibe')
    else:
        print('Estas en el grupo B, pibe.')