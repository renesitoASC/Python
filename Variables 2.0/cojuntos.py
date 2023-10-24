# Para meter un conjunto dentro de otro conjunto debo aplicar la funcion "frozenset", que congela el conjunto y lo hace INMUTABLE.
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = ([conjunto1,"dato3"])

print(conjunto2)

# Teoria de conjuntos

conjunto1 = {1,2,3,7}
conjunto2 ={1,3,7}

# Forma para comprobar si es un subconjunto
subconjunto = conjunto2.issubset(conjunto1)
subconjunto_forma_2 = conjunto2 <= conjunto1

print(subconjunto)

# Verificando si es un superconjunto
superconjunto = conjunto1.issuperset(conjunto2)
superconjunto_forma_2 = conjunto1 > conjunto2

print(superconjunto) 

# Verificar si hay algun numero en comun. SI hay aunque sea 1 elemento que coincida devuelve falso.
numero_igual = conjunto2.isdisjoint(conjunto1)

print(numero_igual)