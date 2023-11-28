import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Graficos\\ingresos.csv')

sns.barplot(x='fuente',y='ingresos',data=df) # Al crear graficos siempre se mantienen los mismos parametros
total_ingresos = df['ingresos'].sum()

print(f'el total de ingresos es de: {total_ingresos} USD.')
plt.show()