# Lo que tarda una persona en decir 2 palabras
tiempo_en_decir_dos_palabras = 1

# Le pido al usuario que diga una frase
print(" ")
pedir_frase = input("Por favor ingresa una frase: ")

# Separando las palabras
cantidad_de_palabras = pedir_frase.split(" ")

# Calculando cuantas palabras dijiste
total_de_palabras = len(cantidad_de_palabras)


if total_de_palabras / 2 > 60:
    print(" ")
    print("No te pedi un testamento")
elif total_de_palabras / 2 < 60:
    print(" ")
    print(f"La cantida de palabras que dijiste fueron: {total_de_palabras}")
    print(f"Tardarias {total_de_palabras/2} segundos en decirla.")
    
tiempo_dalto = 0.7 * 100 / 10 / total_de_palabras

# Mostrando cuanto tardaria dalto en decirlo
print(f"Dalto tardaria {tiempo_dalto} segundos en decir la misma frase.")