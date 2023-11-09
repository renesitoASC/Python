import pprint
import sys
sys.path.append('c:\\Users\\frank\\OneDrive\\Escritorio\\Python\\Practica_modulos_calculos')
sys.path.append('c:\\Users\\frank\\OneDrive\\Escritorio\\Python\\Practica_modulos_estudio')
sys.path.append('c:\\Users\\frank\\OneDrive\\Escritorio\\Python\\Practica_modulos_saludos')
import Despedia 
import Suma
import Resta
import Lenguaje_c
import Lenguaje_python
import Saludo_cordial as m_saludo_cordial
import Saludo_normal as m_saludo_normal

print('\n1- Calculos matematicos.')
print('2- Saludos al usuario.')
print('3- Te digo que sos dependiendo que lenguaje estudies.')      # MENU PRICIPAL
print('4- Me despido.')

while True:
    print('------------------')
    pregunta_al_usuario = input('Ingrese la opcion que desee realizar: ')

    if len(pregunta_al_usuario) == 1:
        break                                       # Evaluando que ingrese solo UNA opcion.
    else:
        print('Elija solo una opcion por favor.')

if pregunta_al_usuario == '1':
    while True:
        print('\nUsted ha elegido "Calculos matematicos".')
        print('------------')
        print('1- Sumar')
        print('2- Restar')          # Menu para CALCULOS.
        print('------------')
        decision_usuario_calculos = input('Ingrese el calculo que desa realizar: ')

        if len(decision_usuario_calculos) == 1:
            break
        else:
          print('Por favor elija solo un calculo a realizar.')

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
        if len(decision_usuario_saludo) == 1:
            break
        else:
            print('Ingrese un solo tipo de saludo.')

    if decision_usuario_saludo == '1':
        print(m_saludo_cordial.Saludo_cordial())
    elif decision_usuario_saludo == '2':    # Imprimiendo funciones para SALUDOS
        print(m_saludo_normal.Saludo_normal())

