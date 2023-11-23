# Creando dos listas diferentes que contengan nombres y apellidos y luego crear un archvio txt e imprimir los datos en el.

nombres = ['rene','franco','valentina','mateo','agustin']
apellidos = ['ASC','cerana','giardini','barba','Messi']

with open('nombres_y_apellidos.txt','w') as archivo: # Si utilizamos esta funcion de with open y no existe ningun archivo. LO CREA en la ruta actual. 
    for n,a in zip(nombres,apellidos):
        archivo.writelines(f'El nombre es: {n}\n')  # Siempre que querramos que se escriba en el archivo y no lo imprima en el actual, tenemos que
        archivo.writelines(f'El apellido es: {a}\n') # utilizar el metodo 'writelines' seguido del nombre del archivo txt o csv etc.
        archivo.writelines('----------------\n')    