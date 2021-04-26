# import requests as req
from pathlib import Path
import json
import pandas as pd 
import statistics as std
from math import sqrt



data_path = 'https://datos.comunidad.madrid/catalogo/dataset/eb0c86dc-743d-4220-a53f-da43a8cbc955/resource/d12f9a6d-aa9c-404f-82a8-9dcaaffebc28/download/uniones_hecho_parejas.json'
# My dir to save data (.json)
my_path = Path('./analisis parejas/data')

# response = req.get(data_path).json()
# with open(my_path / 'parejas.json', 'w', encoding= "utf8") as json_file:
#     json.dump(response['data'], json_file, ensure_ascii = False)   

dataset = pd.read_json(my_path / 'parejas.json', orient='records')

first_sample=dataset.query('inscripcion_año <= 2010')
second_sample=dataset.query('inscripcion_año > 2010')

#? Proporción de todos los tipos de pareja

n_hetero_first_sample = first_sample.query("pareja_tipo == 'heterosexual'")["num_inscripciones"].sum()
n_homo_fem_first_sample = first_sample.query("pareja_tipo == 'homosexual femenina'")["num_inscripciones"].sum()
n_homo_masc_first_sample = first_sample.query("pareja_tipo == 'homosexual masculina'")["num_inscripciones"].sum()

print(f"\nParejas heterosexual totales hasta 2010: {n_hetero_first_sample}\nParejas homosexual femenina totales hasta 2010: {n_homo_fem_first_sample}\nParejas homosexual masculina totales hasta 2010: {n_homo_masc_first_sample}")

n_hetero_second_sample = second_sample.query("pareja_tipo == 'heterosexual'")["num_inscripciones"].sum()
n_homo_fem_second_sample = second_sample.query("pareja_tipo == 'homosexual femenina'")["num_inscripciones"].sum()
n_homo_masc_second_sample = second_sample.query("pareja_tipo == 'homosexual masculina'")["num_inscripciones"].sum()

print(f"\nParejas heterosexual totales desde 2011: {n_hetero_second_sample}\nParejas homosexual femenina totales desde 2011: {n_homo_fem_second_sample}\nParejas homosexual masculina totales desde 2011: {n_homo_masc_second_sample}")

n_first_sample = first_sample["num_inscripciones"].sum()
n_second_sample = second_sample["num_inscripciones"].sum()

print(f"\nParejas totales hasta 2010: {n_first_sample}\nParejas totales desde 2011: {n_second_sample}")

p_hetero_first_sample = n_hetero_first_sample/ n_first_sample
p_homo_fem_first_sample = n_homo_fem_first_sample/ n_first_sample
p_homo_masc_first_sample = n_homo_masc_first_sample/ n_first_sample

print(f"\nProporcion parejas heterosexuales hasta 2010: {p_hetero_first_sample:.2f}\nProporcion parejas homosexuales femeninas hasta 2010: {p_homo_fem_first_sample:.2f}\nProporcion parejas homosexuales masculinas hasta 2010: {p_homo_masc_first_sample:.2f}")

p_hetero_second_sample = n_hetero_second_sample/ n_second_sample
p_homo_fem_second_sample = n_homo_fem_second_sample/ n_second_sample
p_homo_masc_second_sample = n_homo_masc_second_sample/ n_second_sample

print(f"\nProporcion parejas heterosexuales desde 2011: {p_hetero_second_sample:.2f}\nProporcion parejas homosexuales femeninas desde 2011: {p_homo_fem_second_sample:.2f}\nProporcion parejas homosexuales masculinas desde 2011: {p_homo_masc_second_sample:.2f}")

#? Proporción año a año de parejas heterosexuales y parejas homosexuales

x_years= dataset.drop_duplicates('inscripcion_año', inplace = False, keep = 'first')['inscripcion_año'].tolist()

y_hetero_per_year = []
for date in sorted(x_years):
    y_hetero_per_year.append(dataset.query(f'inscripcion_año == {date} and pareja_tipo == "heterosexual"')["num_inscripciones"].sum())

y_homo_per_year = []
for date in sorted(x_years):
    y_homo_per_year.append(dataset.query(f'inscripcion_año == {date} and pareja_tipo != "heterosexual"')["num_inscripciones"].sum())
    

def get_proportion(hetero,homo,years):
    data_couples = zip(hetero,homo)
    results_list=[]
    count=0
    for couple in data_couples:
        hetero_percentage = (couple[0])/(couple[0]+couple[1])
        homo_percentage = 1-hetero_percentage
        results_list.append({"Year":f"{years[count]}", "Hetero_percentage": hetero_percentage,"Homo_percentage":homo_percentage})
        count +=1
    return results_list

annual_proportion = pd.DataFrame(get_proportion(y_hetero_per_year,y_homo_per_year,x_years))

print(f"\n{annual_proportion.head()}")


#? Considerar si es "aplicable" o no el estadístico de correlación "R" y en tal caso calcularlo

# print(f"\nValor de r de las parejas heterosexuales hasta 2010: {up_to_2010_hetero.r_pearson:.2f}")    
# print(f"Valor de r de las parejas homosexuales hasta 2010: {up_to_2010_homo.r_pearson:.2f}")
# print(f"Valor de r de las parejas heterosexuales desde 2011: {from_2010_hetero.r_pearson:.2f}")
# print(f"Valor de r de las parejas homosexuales desde 2011: {from_2010_homo.r_pearson:.2f}")

####? Z

p1 = p_homo_fem_first_sample + p_homo_masc_first_sample
p2 = p_homo_fem_second_sample + p_homo_masc_second_sample

P = (n_first_sample*p1 + n_second_sample*p2)/(n_first_sample+n_second_sample)

Z = (p2-p1)/sqrt(P*(1-P)*(1/n_first_sample+1/n_second_sample))

print(Z)