import requests as req
from pathlib import Path
import json
import statistics as std
from math import sqrt
from functools import reduce


data_path = 'https://datos.comunidad.madrid/catalogo/dataset/eb0c86dc-743d-4220-a53f-da43a8cbc955/resource/d12f9a6d-aa9c-404f-82a8-9dcaaffebc28/download/uniones_hecho_parejas.json'
# My dir to save data (.json)
my_path = Path('./analisis parejas/data')

# response = req.get(data_path).json()
# with open(my_path / 'parejas.json', 'w', encoding= "utf8") as json_file:
#     json.dump(response['data'], json_file, ensure_ascii = False)   

def first_sample(year,datafile):
    for couple in datafile:
        yield couple if couple["inscripcion_año"] <= year else None
        
def second_sample(year,datafile):
    for couple in datafile:
        yield couple if couple["inscripcion_año"] > year else None
            
def n_inscriptions(datafile, couple_type = "h"):
    for couple in datafile:
        yield int(couple["num_inscripciones"]) if couple and couple["pareja_tipo"].startswith(couple_type) else 0
            
def n_cancelations(datafile, couple_type = 'h'): 
    for couple in datafile:
        yield int(couple["num_inscripciones_cancelacion"]) if couple and couple["pareja_tipo"].startswith(couple_type) else 0
    
# def get_proportion(couple_type, datafile, option):
#     n_couples = get_total_couples(datafile)
#     if option == "inscriptions":
#         return sum(list(n_inscriptions(datafile,couple_type))) / n_couples
#     elif option == "cancelations":
#         return sum(list(n_cancelations(datafile,couple_type))) / n_couples

# def annual_proportion_generator(couple_type = 'h', years, datafile, option = "inscriptions"):
#     for year in years:
#         annual_sample = list(filter(lambda couple: couple["inscripcion_año"] == year, datafile))
#         yield f'{get_proportion(couple_type, annual_sample, option):.2f}'

#     if couple_type != "h":
#         for couple in sample_by_couple_type(couple_type, datafile):
#             yield int(couple["num_inscripciones_cancelacion"])
#     else:
#         for couple in datafile:
#             yield int(couple["num_inscripciones_cancelacion"])
        

# with open(my_path / 'parejas.json', 'r', encoding="utf8") as file:
#     data = json.load(file)

#     cut_year = "2010"
    
#     #? Establecer dos muestras una desde el inicio del dataset hasta 2010 inclusive y otra desde 2011 en adelante
    
#     # first_sample = list(filter(lambda couple: couple["inscripcion_año"] <= cut_year, data))  #*| Obtenemos las dos muestras usando
#     # second_sample = list(filter(lambda couple: couple["inscripcion_año"] > cut_year, data))  #*| filter con lambda.
    
#     first_sample = list(first_sample(cut_year,data) )    #*| Asignamos a las variables first_sample y second_sample su
#     second_sample = list(second_sample(cut_year,data) )  #*| funcion generator para utilizarla luego cuando se requiera.
    
    
#     #? Obtener la proporción de todos los tipos de pareja

#     # print(f'\nProporción Heterosexuales hasta 2010: {get_proportion("he", first_sample):.2f}')
#     # print(f'Proporción Homosexual femenina hasta 2010: {get_proportion("homosexual f", first_sample):.2f}')
#     # print(f'Proporción Homosexual masculina hasta 2010: {get_proportion("homosexual m", first_sample):.2f}')

#     # print(f'\nProporción Heterosexuales desde 2011: {get_proportion("he", second_sample):.2f}')
#     # print(f'Proporción Homosexual femenina desde 2011: {get_proportion("homosexual f", second_sample):.2f}')
#     # print(f'Proporción Homosexual masculina desde 2011: {get_proportion("homosexual m", second_sample):.2f}')

#     #? Obtener la proporción año a año de parejas heterosexuales y parejas homosexuales
    
#     years_list = sorted(set(map(lambda couple: couple["inscripcion_año"], data)))

#     hetero_per_year = annual_proportion_generator("he", years_list, data)
#     homo_fem_per_year = annual_proportion_generator("homosexual f", years_list, data)
#     homo_masc_per_year = annual_proportion_generator("homosexual m", years_list, data)
    
#     #? Obtener proporción de cancelaciones 

#     cancel_hetero_per_year = annual_proportion_generator(couple_type='he',years_list, data, option="cancelatios")
    
    



    
    