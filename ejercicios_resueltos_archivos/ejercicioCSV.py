import pandas as pd

df = pd.read_csv('ejercicios_resueltos_archivos\\texto_de_csv.csv')

# Cambiandole el tipo de dato de una columna
df['edad'] = df['edad'].astype(str)

print(type(df['edad'][0]))

# Reemplazando el apellido del primer parametro, por el segundo. MUY IMPORTANTE INGRESAR EL 'inplace=True' para que funcione.
df['apellido'].replace('giardini','puta',inplace=True)

# Eliminando las FILAS con datos faltantes.
df = df.dropna() 

# Eliminando las FILAS con datos repetidos
df = df.drop_duplicates()

# TIP: para eliminar las COLUMNAS con datos faltantes seria asi: (Es muy raro hacer esto ya que se eliminaria toda la columna.)
# df = df.dropna(axis=1) En este caso el 1 = columnas, y el 0 = filas.

# Creando un archivo CSV con el DATAFRAME limpio.
df.to_csv('ejercicios_resueltos_archivos\\datos_csv_limpios.csv') 