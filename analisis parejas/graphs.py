import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
from main import dataset, x_years, y_hetero_per_year, y_homo_per_year, annual_proportion


#? Graficar el ejercicio 4 y ejercicio 5 (este último solo si es lineal)

# 4 #? UP TO 2010 dividido solo entre heterosexuales y homosesuales
labels = 'Heterosexuales', 'Homosexuales'
sizes = [dataset.query(f'inscripcion_año <= 2010 and pareja_tipo == "heterosexual"')["num_inscripciones"].sum(),dataset.query(f'inscripcion_año <= 2010 and pareja_tipo != "heterosexual"')["num_inscripciones"].sum()]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


# 4 #? FROM 2010 dividido solo entre heterosexuales y homosesuales
labels = 'Heterosexuales', 'Homosexuales'
sizes = [dataset.query(f'inscripcion_año > 2010 and pareja_tipo == "heterosexual"')["num_inscripciones"].sum(),dataset.query(f'inscripcion_año > 2010 and pareja_tipo != "heterosexual"')["num_inscripciones"].sum()]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


# 5 #? Número de parejas heterosexuales y homosexuales por año
mplstyle.use('dark_background')
plt.plot(x_years,y_hetero_per_year,'y',label="heterosexuales")
plt.plot(x_years,y_homo_per_year,'b',label="homosexuales")
plt.title('Inscripciones de parejas (heterosexuales y homosexuales)')
plt.xlabel('años')
plt.ylabel('nº inscripciones totales')
plt.legend()

# 5 #? PORCENTAJE de parejas heterosexuales y homosexuales por año
mplstyle.use('dark_background')
plt.plot(x_years,annual_proportion["Hetero_percentage"].tolist(),'y',label="heterosexuales")
plt.plot(x_years,annual_proportion["Homo_percentage"].tolist(),'b',label="homosexuales")
plt.title('Inscripciones de parejas (heterosexuales y homosexuales)')
plt.xlabel('años')
plt.ylabel('nº inscripciones totales')
plt.legend()

plt.show()
