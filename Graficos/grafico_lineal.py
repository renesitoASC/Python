import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Graficos\\fechas_pedos.csv') # Abrimos el archivo csv
print(df)

sns.lineplot(x='fecha',y='pedos',data=df) # Creamos un grafico lineal

plt.plot('16-01',17,'o') # Creamos un punto en la vez donde mas se tiro pedos
plt.show() # Mostramos el grafico
