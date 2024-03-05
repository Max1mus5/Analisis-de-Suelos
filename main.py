from API.client import get_data
from Utils.input import userInput
from Utils.data import calcular_mediana_edaficas
import time
from UI.interface import mostrar_tabla

limit = int(input("Ingrese el número de registros a consultar: "))
filters = userInput()
data = get_data(**filters, limit=limit)
if len(data) < limit:
    print("No hay suficientes registros, se mostraran los disponibles:")
    print("Datos obtenidos:")
    data = get_data(**filters, limit=limit)

time.sleep(3)

mediana_edaficas = calcular_mediana_edaficas(data)
""" modificar los nombres de las filas """
mediana_edaficas.index = ['Fósforo (mg/kg)', 'pH', 'Potasio (cmol/kg)']
print("Mediana de variables edáficas:")
print(mediana_edaficas)

""" print("Datos obtenidos:")
print(data[ ["departamento", "municipio", "cultivo", "topografia"] ]) """

mostrar_tabla(data, mediana_edaficas)