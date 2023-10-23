barra_pan = 3.49
barra_pan_vieja = 60 / 100 * 3.49

pan_dia = int(input("Ingrese la cantidad de pan que ha adquirido del dia: "))
pan_viejo = int(input("Ingrese la cantidad de pan que ha adquirido que no sea del dia: "))

costo_total = barra_pan * pan_dia + barra_pan_vieja * pan_viejo

print("------------------")
print(f"El precio habitual de una barra de pan esta en: {barra_pan} euros")
print(f"Se le hace un descuento del 60 %, es decir de {barra_pan_vieja} euros")
print(f"El precio a pagar es de: {costo_total} euros")

