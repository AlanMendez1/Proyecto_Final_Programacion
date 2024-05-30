import random
import string

def generar_contrasena():
    longitud = 8
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

def generar_servicio(servicio):
    contrasena = generar_contrasena()
    print(f"Servicio: {servicio}\nContraseña: {contrasena}\n")

servicios = ["Netflix", "Google", "Outlook", "HBO"]

for servicio in servicios:
    generar_servicio(servicio)
