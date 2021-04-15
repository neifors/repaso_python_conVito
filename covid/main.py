import requests as req
from pathlib import Path
import json
import pandas as pd 
import matplotlib.pyplot as plt
import statistics as std
import matplotlib.style as mplstyle


# URL 26FEB - 1JUL
data_path1 = 'https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json'
# URL FROM 2JUL
data_path2 = 'https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/877fa8f5-cd6c-4e44-9df5-0fb60944a841/download/covid19_tia_muni_y_distritos_s.json'
# My dir to save data (.json)
my_path = Path('./covid/data')

###? DATOS DEL PRIMER DATASET (FEB-JUL)
# response = req.get(data_path1).json()
# with open(my_path / 'covid_feb-jul.json', 'w') as json_file:
#     json.dump(response['data'], json_file)   

dataset = pd.read_json(my_path / 'covid_feb-jul.json', orient='records')

# # print(dataset.tail(199)) # <-- Imprime todos los datos en forma de tabla dónde encontramos [Número de filas X número de columnas] al final de ésta

first_total_districts = dataset.drop_duplicates('municipio_distrito', inplace = False, keep = 'first') # Elimina los repetidos y se queda con la PRIMERA vez que aparece cada distrito
last_total_districts = dataset.drop_duplicates('municipio_distrito', inplace = False, keep = 'last')   # Elimina los repetidos y se queda con la ULTIMA vez que aparece cada distrito

# print(f"Número de distritos: {len(last_total_districts)}")  # <-- Número total de distritos
# # print(first_total_districts.shape)   # <-- Número de distritos X número de columnas

# print(f"TIA inicial: {last_total_districts['casos_confirmados_totales'].sum()}")
# print(f"TIA final: {first_total_districts['casos_confirmados_totales'].sum()}")

date_list = dataset.drop_duplicates('fecha_informe', inplace = False, keep = 'first')['fecha_informe'].tolist()
# # print(sorted(date_list)) # <-- lista 'fecha_informe' con formato "yyyy/mm/dd hh:mm:ss" ordenada
# print(f'Número total de dias registrados: {len(date_list)}')

short_date_list = [date.split(' ')[0][5:] for date in date_list] # <-- Lista con las fechas de registro en formato mm/dd 
x_axis = list(range(len(date_list)))  # <-- Lista con números de 0 a n-1 siendo n el número total de dias en los que ha habido registro

y_axis = []
for date in sorted(date_list):
    y_axis.append(int(dataset.query(f'fecha_informe == "{date}"')['casos_confirmados_totales'].sum()))

to_may = std.Statistics(x_axis[:66],y_axis[:66])
print(to_may.x_times_y)
# from_may = std.Statistics(x_axis[65:],y_axis[65:])

# print(f'\nCoeficiente de Pearson Feb-1,May: {to_may.r_pearson:.2f}')
# print(f'Coeficiente de Pearson 1,May-1-Jul: {from_may.r_pearson:.2f}')

# print(f'\nB Feb-1,May: {to_may.b:.2f}')
# print(f'B 1,May-1-Jul: {from_may.b:.2f}')


# mplstyle.use('dark_background')
# plt.plot(x_axis[:66],y_axis[:66],'y',label="from 26, Feb")
# plt.plot(x_axis[65:],y_axis[65:],'b',label="from 1, May")
# plt.title('Curva COVID - Madrid')
# plt.xlabel('Dias')
# plt.ylabel('Casos confirmados totales')
# plt.legend()
# plt.show()

###? DATOS DEL PRIMER DATASET (FROM JUL)

# response = req.get(data_path2).json()
# with open(my_path / 'covid_from-jul_weekly.json', 'w') as json_file:
#     json.dump(response['data'], json_file)   

dataset2 = pd.read_json(my_path / 'covid_from-jul_weekly.json', orient='records')

# print(dataset2['municipio_distrito'].value_counts().tail(20)) 
# print(dataset)

# {"municipio_distrito": "Madrid-Retiro", "codigo_geometria": "079603", "tasa_incidencia_acumulada_ultimos_14dias": 23.4668991007149, "tasa_incidencia_acumulada_total": 1417.23308497532, "casos_confirmados_totales": 1691, "casos_confirmados_ultimos_14dias": 28, "fecha_informe": "2020/07/01 09:00:00"}
# {"municipio_distrito": "Madrid-Retiro", "codigo_geometria": "079603", "tasa_incidencia_acumulada_ultimos_14dias": 293.336238758936, "tasa_incidencia_acumulada_total": 8950.94579984411, "casos_confirmados_totales": 10680, "casos_confirmados_ultimos_14dias": 350, "fecha_informe": "2021/04/06 11:56:00"}

