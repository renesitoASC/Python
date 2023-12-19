lista = [1,1,2,3,5,8,13,21,34,55,89]
nueva_lista = []
lista2 = []

for num in lista:
    if num < 5:
        nueva_lista.append(num)
    else:
        pass

print(nueva_lista)

pedir_numero = int(input('Ingrese un numero: '))
for num in lista:
    if num < pedir_numero:
        lista2.append(num)
    else:
        pass
print(lista2)