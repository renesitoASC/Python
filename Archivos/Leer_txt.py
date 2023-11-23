archivo = open('Archivos\\texto_de_rene.txt',encoding='UTF-8')# Esto ultimo agregado tiene que ver con la codificacion global.(para que no tire errores en el texto)
# print(archivo_sin_abrir) # Asi NO se imprime lo que contenga dicho archivo. Sino que asi:

# Leer archivo completo
#archivo_abierto = archivo_sin_abrir.read() Lo pongo en comentario porque una vez que se lee, se cierra el archivo y no puede volver abrirse.
#print(archivo_abierto)

# Leer linea por linea
lineas = archivo.readlines()

# Leer una sola linea del archivo 
una_sola_linea = archivo.readline()

# Cerrar el archivo, importante para que no ocurran problemas.
archivo.close()
