from operator import truediv
import pprint
import sys
sys.path.append('c:\\Users\\frank\\OneDrive\\Escritorio\\Python\\Practica_modulos_calculos')
sys.path.append('c:\\Users\\frank\\OneDrive\\Escritorio\\Python\\Practica_modulos_estudio')
sys.path.append('c:\\Users\\frank\\OneDrive\\Escritorio\\Python\\Practica_modulos_saludos')
import Despedia 
import Suma
import Resta
import Lenguaje_c as opcion_c
import Lenguaje_python as opcion_py
import Saludo_cordial as m_saludo_cordial
import Saludo_normal as m_saludo_normal

print('\n1- Calculos matematicos.')
print('2- Saludos al usuario.')
print('3- Te digo que sos dependiendo que lenguaje estudies.')      # MENU PRICIPAL
print('4- Me despido.')

while True:
    print('------------------')
    pregunta_al_usuario = input('Ingrese la opcion que desee realizar: ')

    if len(pregunta_al_usuario) == 1 and pregunta_al_usuario in ['1','2','3','4']:
        break                                       # Evaluando que ingrese solo UNA opcion.
    else:
        print('Elija una opcion valida por favor.')

if pregunta_al_usuario == '1':
    while True:
        print('\nUsted ha elegido "Calculos matematicos".')
        print('------------')
        print('1- Sumar')
        print('2- Restar')          # Menu para CALCULOS.
        print('------------')
        decision_usuario_calculos = input('Ingrese el calculo que desa realizar: ')

        if len(decision_usuario_calculos) == 1 and decision_usuario_calculos in ['1','2']:
            break
        else:
          print('Por favor elija un calculo a realizar valido.')

    if decision_usuario_calculos == '1':
        print(Suma.Funcion_suma())          # Imprimiendo funciones para CALCULOS
    elif decision_usuario_calculos == '2':
        print(Resta.Funcion_resta())

if pregunta_al_usuario == '2':
    while True:
        print('\nUsted ha elegido "Saludos al usuario"')
        print('------------')
        print('1- Saludo cordial.')
        print('2- Saludo normal.')          # Menu para SALUDOS
        print('------------')
        decision_usuario_saludo = input('Ingrese el tipo de saludo que quiere recibir: ')
        if len(decision_usuario_saludo) == 1 and decision_usuario_saludo in ['1','2']:
            break
        else:
            print('Ingrese un tipo de saludo valido por favor.')

    if decision_usuario_saludo == '1':
        print(m_saludo_cordial.Saludo_cordial())
    elif decision_usuario_saludo == '2':    # Imprimiendo funciones para SALUDOS
        print(m_saludo_normal.Saludo_normal())

if pregunta_al_usuario == '3':
    while True:
        print('\nUsted ha elegido "Te digo que sos dependiendo que lenguaje estudies."')
        print('------------')
        print('1- Estudio lenguaje Python.')
        print('2- Estudio lenguaje C.')     # Menu para LENGUAJES
        print('------------')
        decision_usuario_lenguaje = input('Ingrese el lenguaje que esta estudiando: ')
        if len(decision_usuario_lenguaje) == 1 and decision_usuario_lenguaje in ['1','2']:
            break
        else:
            print('Por favor ingrese solo un lenguaje valido (1 o 2).')
        
    if decision_usuario_lenguaje == '1':
        print(opcion_py.Lenguaje_python())
    elif decision_usuario_lenguaje == '2':  # Imprimiendo funciones para LENGUAJES
        print(opcion_c.Lenguaje_c())
        
if pregunta_al_usuario == '4':
        print('\nUsted ha elegido "Despido".')  # Opcion 4 que solo imprime la llamada al modulo y a su unica variable.
        print(Despedia.variable_despedida)
        