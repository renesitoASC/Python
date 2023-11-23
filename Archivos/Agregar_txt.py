with open('Archivos\\texto_de_rene.txt','a') as archivo: # Ahora con la 'a' lo que hacemos es AGREGAR
    for i in range(5):
        archivo.write(f'\nAgregando linea {i+1}')
