with open('Archivos\\texto_de_rene.txt','w') as archivo:  # La 'w' seguida de la coma dentro de los parametros de open() significa que vamos a SOBREESCRIBIR el archivo.
    
    archivo.write('Sobrescribiendo el archivo con el metodo write') # Con este metodo ESCRIBIMOS el archivo.
    
    archivo.writelines(['\nCon este otro metodo agregamos lineas al archivo.','\nLe podemos pasar las oraciones que queramos porque es un iterable'])