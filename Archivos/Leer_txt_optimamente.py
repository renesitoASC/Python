with open('Archivos\\texto_de_rene.txt',encoding='UTF-8') as archivo_texto: # El 'as' aqui se usa como siempre para cambiarle el nombre.
    contenido = archivo_texto.read()

    print(contenido)    # Las funciones se van a realizar solo si se abrio correctamente el archivo.
                        # Una vez que se terminan de realizar todas las funciones se cierra el archivo automaticamente, por eso es optimo.
