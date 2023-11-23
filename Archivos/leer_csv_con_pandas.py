import pandas as pd
df = pd.read_csv('Archivos\\texto_de_csv.csv')  # 'df' significa 'Data Frame'
df2 = pd.read_csv('Archivos\\texto_de_csv.csv')

nombres = df['nombre']  # Aqui obtenemos los datos SOLAMENTE de la columna 'nombres'
apellidos = df['apellido']  # Aqui obtenemos los datos SOLAMENTE de la columna 'apellido'
edad = df['edad']   # Aqui obtenemos los datos SOLAMENTE de la columna 'edad'

# Ordenando el dataframe por la edad de forna ASCENDENTE
df_ordenado_ascendente = df.sort_values('edad')

# Ordenando el dataframe por la edad de forma DESCENDIENTE
df_ordenando_descendiente = df.sort_values('edad',ascending=False) # Para ordenar de mayor a menor tenemos que agregar un segundo parametro luego de la coma y ponerle False.

# Concatenando DF
df_concatenado = pd.concat([df,df2]) # Utilizamos un metodo pero directamente al modulo pd que seria pandas.

# Accediendo a las primeras filas con head()
accediendo_a_filas_del_df = df.head(3)  # En el parametro ingresamos las filas a las cuales querramos leer.

# Accediendo a las primeras filas con tail()
accediendo_a_filas_del_df_ultimas = df.tail(1)

# Accediendo a la cantidad de filas y columnas en el df con shape()
filas_y_columnas_totales = df.shape
filas_totales = filas_y_columnas_totales[0]
columnas_totales = filas_y_columnas_totales[1]

filas_totales,columnas_totales = df.shape   # Lo que hice aca fue DESEMPAQUETAR. Seria lo mismo que lo de arriba pero mas rapido.

# Obteniendo data estadistica del df. (SIRVE PARA ANALISIS DE DATOS.)
df_info = df.describe()

# Accediendo a un elemento especifico del df con loc
elemento_especifico = df.loc[0,'edad']  # En el primer parametro se ingresa el numero de la fila a imprimir, y en el segundo parametro la columna elegida.

# Accediendo a un elemento especifico del df con iloc (que es a traves de SOLO INDICES de las filas y columnas)
elemento_especifico_a_traves_de_indices = df.iloc[1,0]

# Accediendo a TODAS las filas de UNA columna con slicing
accediendo_a_todos_los_apellidos = df.iloc[:,1]

# Accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

# Accediendo a filas mayores que 30 años
edades_mayores_30 = df.loc[df['edad']>30,:]

print(edades_mayores_30)