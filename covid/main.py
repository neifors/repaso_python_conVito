import requests as req
from pathlib import Path
import json
import pandas as pd 
import matplotlib.pyplot as plt
import statistics as std
import matplotlib.style as mplstyle



data_path = 'https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json'
backup_path = Path('./covid/data/my_data.json')

# response = req.get(data_path).json()

# with open(backup_path, 'w') as json_file:
#     json.dump(response['data'], json_file)
    
dataset = pd.read_json(backup_path, orient='records')
# print(dataset.tail(199)) # <-- Imprime todos los datos en forma de tabla dónde encontramos [Número de filas X número de columnas] al final de ésta

first_total_districts = dataset.drop_duplicates('municipio_distrito', inplace = False, keep = 'first') # Elimina los repetidos y se queda con la PRIMERA vez que aparece cada distrito
last_total_districts = dataset.drop_duplicates('municipio_distrito', inplace = False, keep = 'last')   # Elimina los repetidos y se queda con la ULTIMA vez que aparece cada distrito

print(f"Número de distritos: {len(last_total_districts)}")  # <-- Número total de distritos
# print(first_total_districts.shape)   # <-- Número de distritos X número de columnas

print(f"TIA inicial: {last_total_districts['casos_confirmados_totales'].sum()}")
print(f"TIA final: {first_total_districts['casos_confirmados_totales'].sum()}")

date_list = dataset.drop_duplicates('fecha_informe', inplace = False, keep = 'first')['fecha_informe'].tolist()
# print(sorted(date_list)) # <-- lista 'fecha_informe' con formato "yyyy/mm/dd hh:mm:ss" ordenada
print(f'Número total de dias registrados: {len(date_list)}')

short_date_list = [date.split(' ')[0][5:] for date in date_list] # <-- Lista con las fechas de registro en formato mm/dd 
x_axis = list(range(len(date_list)))  # <-- Lista con números de 0 a n-1 siendo n el número total de dias en los que ha habido registro


# x_axis = sorted(short_date_list)
# print(x_axis)

y_axis = []
for date in sorted(date_list):
    y_axis.append(int(dataset.query(f'fecha_informe == "{date}"')['casos_confirmados_totales'].sum()))
# print(y_axis)

my_obj = std.Statistics(x_axis,y_axis)
print(f'Media de x: {my_obj.y_mean:.2f}')



mplstyle.use('dark_background')
plt.plot(x_axis[:64],y_axis[:64],'y',label="from 26, Feb")
plt.plot(x_axis[63:],y_axis[63:],'b',label="from 1, May")
plt.title('Curva COVID - Madrid')
plt.xlabel('Dias')
plt.ylabel('Casos confirmados totales')
plt.legend()
plt.show()
