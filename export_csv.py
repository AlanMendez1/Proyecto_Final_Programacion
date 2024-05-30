import csv

def exportar_csv(nombre_archivo, datos, encabezados):
    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            escritor_csv = csv.writer(archivo)
            if encabezados:
                escritor_csv.writerow(encabezados)  # Escribir los encabezados
            escritor_csv.writerows(datos)  # Escribir las filas de datos
        print(f"Archivo {nombre_archivo} exportado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al exportar el archivo: {e}")

# Ejemplo de uso
encabezados = ["Nombre", "Edad", "Ciudad"]
datos = [
    ["Alice", 30, "Madrid"],
    ["Bob", 25, "Barcelona"],
    ["Charlie", 35, "Valencia"]
]

nombre_archivo = 'exportado.csv'
exportar_csv(nombre_archivo, datos, encabezados)
