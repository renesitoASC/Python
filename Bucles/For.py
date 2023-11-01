numeros = [1,2,3,4,5]

animales = ["pato","perro","gato","caballo","raton"]

# El ciclo for en Python a diferencia de otros lenguajes no utiliza los tipicos parametros de (i = 0;i < 0;i++)
for numero in numeros:
    print(numero)
    
# iterando dos listas al mismo tiempo con la funcion zip()
for numero,animal in zip(numeros,animales):
    print(f"Recorriendo la lista 1: {numero}")
    print(f"Recorriendo la lista 2: {animal}")
    
# Iterando una lista a traves de su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")
    
# Utilizando el else en el bucle for
for numero in numeros:
    print(f"El valor es: {numero}")
else:
    print("Fin del bucle")  
    
    
# Todo esto funciona tanto con listas como con tuplas y conjuntos