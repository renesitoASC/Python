import csv

with open('Archivos\\texto_de_csv.csv') as archivo:
    archivo_leido = csv.reader(archivo)
    for row in archivo_leido:
        print(row)
