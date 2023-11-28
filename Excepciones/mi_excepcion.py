class miExcepcion():
    def __init__(self,err):
        print(f'cometiste el siguiente error: {err}')

# Lanzando mi PROPIA excepcion
# raise miExcepcion('jajajaja, persona poco culta')

# Manejando la excepcion
try:
    raise miExcepcion('jajajajaja ,persona poco culta')
except: 
    print('Como vas a cometer ese error?')

