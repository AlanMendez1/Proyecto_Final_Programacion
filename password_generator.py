import random
import string

def generar_contrasena(longitud=8):
    if longitud < 4:
        raise ValueError("La longitud de la contraseña debe ser al menos 4 para incluir todos los tipos de caracteres.")

    # Asegurarse de que al menos un caracter de cada tipo esté incluido
    caracteres = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Rellenar el resto de la contraseña con caracteres aleatorios de todos los tipos
    caracteres += random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=longitud - 4)
    
    # Mezclar los caracteres para evitar patrones predecibles
    random.shuffle(caracteres)
    
    # Convertir la lista de caracteres en una cadena
    contrasena = ''.join(caracteres)
    return contrasena

# Generar y mostrar la contraseña
contrasena = generar_contrasena()
print(f"Contraseña generada: {contrasena}")
