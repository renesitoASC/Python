edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("podes pasar")
else: 
    print("No podes pasar")


ingreso_mensual = float(input("Ingresa tu sueldo (mensualmente): "))

if ingreso_mensual >= 100000:
    print('podes aguantar tranquilamente')
elif ingreso_mensual >= 70000:
    print("Estas bien")
elif ingreso_mensual >= 50000:
    print("Vas a estar complicado")
else: 
    print("Pobre")
    
puntos_de_vida = float(input("Ingresa tu vida: "))
puntos_de_ataque = float(input("Ahora ingresa tus puntos de ataque: "))

if puntos_de_vida >= 1500:
    if puntos_de_ataque >= 250:
        print("Podes derrotar al boss final")
    elif puntos_de_ataque <= 200:
        print("Podes intentarl pero va a estar complicado")
    elif puntos_de_ataque <= 100:
        print("Casi imposible")
    elif puntos_de_ataque <= 50:
        print("Imposible")
    else:
        print("Ni lo intentes.")
elif puntos_de_vida < 1500:
    if puntos_de_ataque > 800:
        print("No te tiene que golpear, pero lo oneshoteas.")
else:
    print("Vida insuficiente")
     
  # prueba      

 

