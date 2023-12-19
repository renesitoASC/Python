palabra = input('Ingrese una palabra: ')
lista = list(palabra)

if palabra == lista.reverse():
    print('Su palabra es un palindromo')
else:
    print('Su palabra NO es un palindromo.')