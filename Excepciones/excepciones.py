def sumar_dos(): # creando funcion que suma numeros
    while True:
        a = input('Ingrese un numero: ')
        b = input('Ingrese un segundo numero: ')
        try: # Intentando convertirlos a enteros y sumarlos
            resultado = int(a) + int(b)
        except: # Si lanza una excepcion (error) imprimir lo siguiente.
            print('Ingresa un numero valido por favor.')
        else: # Si todo salio bien salimos del bucle.
            break
        return resultado
 