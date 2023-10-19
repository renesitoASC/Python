# Creando una lista con list()
lista = list(['hola',2,7.8,True])

# Verificando cuantos elementos tiene la lista
len(lista)

# Agregando un elemento a la lista con APPEND (UN SOLO ELEMENTO)
lista.append('asc')

# Agregando un elemento a la lista con INSERT en un indice especifico
lista.insert(2,'ASC')

# Agregando elementos a la lista con EXTEND a traves de una lista
lista.extend([2,False])

# Elimina un elemento de la lista segun su INDICE
lista.pop(0)
 
# Elimina un elemento de la lista por su VALOR
lista.remove(7.8)

# Elimina TODOS los elementos de la lista
lista.clear()

# Ordena los elementos de la lista de forma ascendentes. NO sirve si hay strings en la lista
lista.sort()    # Si usamos el parametro reverse=True los ordena totalmente al reves.

# Invierte todos los elementos de una lista (NO ES LO MISMO QUE CON EL PARAMETRO)
lista.reverse()



print(lista)