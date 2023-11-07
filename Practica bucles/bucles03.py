ingresar_palabra = input('Ingrese una frase: ').lower()
ingresar_letra = input('Ingrese UNA letra: ').lower()

while len(ingresar_letra) > 1:
    print('\nERROR. Ingrese UNA sola letra.')
    ingresar_letra = input('Ingrese UNA letra: ').lower()

resultado = ingresar_palabra.count(ingresar_letra)

print(f'\nEl numero de veces que aparece la {ingresar_letra} en su frase: "{ingresar_palabra}" fue de: {resultado}')
