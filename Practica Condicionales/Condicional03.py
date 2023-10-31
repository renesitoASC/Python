edad_usuario = int(input("Por favor ingrese su edad: "))

ingresos = float(input("Ingrese sus igresos: "))

if edad_usuario > 16:
    if ingresos >= 1000:
        print("Usted tiene que tributar.")
    else: 
        print("Usted no tiene que tributar.")
else:
    print("Usted no tiene que tributar.")
    