ingredientes_no_vegetariana = ['peperoni','jamon','salmon']
ingredientes_vegetariana = ['pimiento','tofu']
ingrediete_elegido = []

opcion_de_pizza = input('Va a querer una pizza vegetariana? (si/no): ').lower()


if opcion_de_pizza.startswith('n'):

    while len(ingrediete_elegido) < 1:
        print(f'\nLos ingredientes que pueden acompañar a la pizza son peperoni,jamon o salmon')
        print('--------------------')

        opcion_de_ingrediente = input('Ingrese UN SOLO ingrediente para que acompañe la pizza: ').lower()

        if opcion_de_ingrediente in ingredientes_no_vegetariana:
            ingrediete_elegido.append(opcion_de_ingrediente)
        else: 
            print('Ingrese un ingrediente disponible. Recuerde que solo puede elegir 1 ingrediente.')

    print(f'\nUsted ha seleccionado una pizza no vegetariana con {ingrediete_elegido[0]}')
            
if opcion_de_pizza.startswith('s'):

    while len(ingrediete_elegido) < 1:
        print(f'\nLos ingredientes que pueden acompañar a la pizza son pimiento y tofu')
        print('--------------------')

        opcion_de_ingrediente = input('Ingrese UN SOLO ingrediente para que acompañe la pizza: ').lower()

        if opcion_de_ingrediente in ingredientes_vegetariana:
            ingrediete_elegido.append(opcion_de_ingrediente)
        else: 
            print('Ingrese un ingrediente disponible. Recuerde que solo puede elegir 1 ingrediente.')

    print(f'\nUsted ha seleccionado una pizza no vegetariana con {ingrediete_elegido[0]}')


