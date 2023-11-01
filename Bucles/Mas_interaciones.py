frutas = ['manzana','banana','pera','granada','naranja']
cadena = 'ASC'
numeros = [2,5,10,20]

# Usando la sentencia 'Continue' hacemos que si se cumple dicha condicion, que el codigo saltee lo que pide.
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'Me voy a comer una {fruta}')
    
# Usando la sentencia 'Break' evitamos que el codigo se siga ejecutando si la condicion se cumple.
for fruta in frutas:
    if fruta == 'pera':
        break
    print(f"Ahora me voy a comer una: {fruta}")
print("Termino el bucle porque me comi una pera")
