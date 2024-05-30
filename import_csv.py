import csv

def leer_csv(nombre_archivo):
    try:
        with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            encabezados = next(lector_csv)  # Leer la primera fila como encabezados
            print("Encabezados:", encabezados)
            for fila in lector_csv:
                print("Fila:", fila)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

nombre_archivo = input("Escribe el nombre de archivo con su extensión .csv: ")
leer_csv(nombre_archivo)
